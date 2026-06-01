---
name: analizar-archivos-existentes
description: "Analiza archivos que el usuario ya tiene: Excel (.xlsx/.xls), PowerPoint (.pptx) y PDF. Extrae contenido, resume, compara, valida métricas y propone próximos pasos (reportes, slides, planes). Usa cuando el usuario diga 'analiza este archivo', 'qué dice este Excel/PPT/PDF', 'compara estos archivos', 'extrae los datos', o adjunte un archivo Office/PDF para entenderlo."
---

# Analizar Archivos Existentes

## Propósito

El gerente de desarrollo recibe constantemente Excel con métricas, decks de leadership, PDFs de contratos / postmortems / RFCs. Esta skill te convierte en su analista: **leer el archivo, entender lo que dice, y entregarle valor accionable** (resumen ejecutivo, métricas extraídas, riesgos, comparativas, o input para otro entregable).

Tu salida es:
1. Un **script Python** que extrae el contenido del archivo a texto/tablas legibles.
2. Un **análisis estructurado** del contenido (no solo el dump crudo).
3. Una **propuesta de siguientes pasos** (¿generar otro reporte? ¿slides? ¿correo ejecutivo?).

## Contexto

Casos típicos del usuario:
- "Mi VP me mandó este Excel de presupuesto, ¿qué riesgos ves?"
- "Tengo el deck del trimestre pasado, sácame los KPIs para comparar con este."
- "Este PDF de 80 páginas es el contrato del proveedor, dime los SLAs y penalidades."
- "Tengo 5 reportes de status semanal en PPTX, compara la evolución de los riesgos."
- "Lee este postmortem en PDF y arma un resumen para mi staff."

## Instrucciones generales

1. **Antes de generar código, pregunta SOLO lo crítico** (no preguntes lo obvio):
   - ¿Cuál es la ruta del archivo? (o adjúntalo / arrástralo a VS Code).
   - ¿Qué busca específicamente? (resumen, métricas concretas, comparación, validación, extracción de tablas).
   - ¿A quién va el output? (afecta tono y nivel de detalle del análisis).
   - Si son varios archivos: ¿comparar entre ellos o consolidar?

2. **Elige la librería correcta según extensión**:

   | Tipo | Extensión | Librería | Notas |
   |---|---|---|---|
   | Excel moderno | `.xlsx` | `openpyxl` | Lee valores, fórmulas, formato, gráficos |
   | Excel legado | `.xls` | `xlrd==1.2.0` o convertir a `.xlsx` | `xlrd` >=2.0 ya no soporta `.xls` |
   | Excel con muchas hojas/datos | cualquiera | `pandas.read_excel` | Más cómodo para análisis tabular |
   | PowerPoint | `.pptx` | `python-pptx` | Extrae texto de shapes, tablas, notas del orador |
   | PowerPoint legado | `.ppt` | Pedir al usuario que lo guarde como `.pptx` | `python-pptx` no soporta `.ppt` |
   | PDF con texto | `.pdf` | `pypdf` (simple) o `pdfplumber` (tablas) | `pdfplumber` es mejor para extraer tablas |
   | PDF escaneado (imágenes) | `.pdf` | `pytesseract` + `pdf2image` | Requiere OCR; avísale al usuario que es más lento |

3. **Instalación de dependencias** (la primera vez):
   ```bash
   pip install openpyxl pandas python-pptx pypdf pdfplumber
   # Solo si el PDF es escaneado:
   pip install pytesseract pdf2image
   ```

4. **Estructura del script** (siempre):
   ```python
   from pathlib import Path
   # imports específicos según el tipo

   ARCHIVO = Path(r"ruta/al/archivo")

   # === EXTRACCIÓN ===
   # ... lógica para sacar texto/tablas/metadata

   # === ANÁLISIS ===
   # ... resumen, métricas calculadas, comparaciones

   # === SALIDA ===
   # Imprimir resumen legible o guardar a markdown/json
   print("=== RESUMEN ===")
   # ...
   ```

5. **Después de ejecutar la extracción, NO te detengas en el dump crudo**. Sintetiza:
   - **TL;DR** (3 líneas máximo).
   - **KPIs / cifras clave** en tabla.
   - **Riesgos / banderas rojas** detectados.
   - **Preguntas abiertas** que el usuario debería investigar.
   - **Próximos pasos sugeridos** (ej. "¿quieres que arme un Excel comparativo?" o "¿genero un resumen ejecutivo en PPTX?").

6. **Encadenamiento con otras skills**: Si tras el análisis tiene sentido producir un nuevo artefacto, propón explícitamente usar:
   - `generar-reporte-excel` para consolidar datos en una nueva hoja.
   - `generar-presentacion-pptx` para resumir hallazgos en un deck.
   - `metricas-dora` si el archivo contiene métricas de delivery.

## Patrones por tipo de archivo

### Excel (`.xlsx`)

```python
import openpyxl
import pandas as pd
from pathlib import Path

ARCHIVO = Path(r"presupuesto-q2.xlsx")

# Opción A: pandas (rápido para análisis tabular)
hojas = pd.read_excel(ARCHIVO, sheet_name=None)  # dict {nombre_hoja: DataFrame}
for nombre, df in hojas.items():
    print(f"\n=== Hoja: {nombre} ({len(df)} filas x {len(df.columns)} cols) ===")
    print(df.head())
    print("Estadísticas numéricas:")
    print(df.describe(include="all"))

# Opción B: openpyxl (cuando importan fórmulas, formato condicional, comentarios)
wb = openpyxl.load_workbook(ARCHIVO, data_only=False)  # data_only=True para valores calculados
for nombre_hoja in wb.sheetnames:
    ws = wb[nombre_hoja]
    print(f"\n=== {nombre_hoja}: {ws.max_row} filas x {ws.max_column} cols ===")
    # Primeras 5 filas como tupla
    for row in ws.iter_rows(min_row=1, max_row=5, values_only=True):
        print(row)
    # Detectar fórmulas
    formulas = [(c.coordinate, c.value) for r in ws.iter_rows() for c in r
                if isinstance(c.value, str) and c.value.startswith("=")]
    if formulas:
        print(f"⚠️ {len(formulas)} celdas con fórmulas. Primeras 3: {formulas[:3]}")
```

**Qué siempre revisar en un Excel ejecutivo**:
- ¿Hay hojas ocultas? (`ws.sheet_state == 'hidden'`)
- ¿Los totales cuadran con la suma de filas? (típico bug de copy-paste).
- ¿Hay valores hardcoded donde debería haber fórmulas?
- ¿Hay fechas mal parseadas (cadenas vs. datetime)?

### PowerPoint (`.pptx`)

```python
from pptx import Presentation
from pathlib import Path

ARCHIVO = Path(r"review-q1.pptx")
prs = Presentation(ARCHIVO)

for i, slide in enumerate(prs.slides, start=1):
    print(f"\n--- Slide {i} ---")
    # Layout (portada, sección, contenido, etc.)
    print(f"Layout: {slide.slide_layout.name}")

    # Texto de todos los shapes
    for shape in slide.shapes:
        if shape.has_text_frame:
            for p in shape.text_frame.paragraphs:
                texto = "".join(run.text for run in p.runs).strip()
                if texto:
                    print(f"  • {texto}")
        # Tablas
        if shape.has_table:
            print("  [TABLA]")
            for row in shape.table.rows:
                print("    | " + " | ".join(c.text.strip() for c in row.cells) + " |")

    # Notas del orador
    if slide.has_notes_slide:
        notas = slide.notes_slide.notes_text_frame.text.strip()
        if notas:
            print(f"  📝 Notas: {notas}")
```

**Qué siempre extraer de un deck**:
- Slide de **portada** → título, periodo, autor.
- Slides con **números grandes** → KPIs.
- **Tablas** → suelen tener riesgos, owners, fechas.
- **Notas del orador** → contexto que no está en pantalla, frecuentemente lo más valioso.

### PDF (`.pdf`)

```python
# Opción A: pypdf — rápido, solo texto
from pypdf import PdfReader
from pathlib import Path

ARCHIVO = Path(r"contrato-proveedor.pdf")
reader = PdfReader(ARCHIVO)
print(f"Páginas: {len(reader.pages)}")
print(f"Metadata: {reader.metadata}")

texto_completo = []
for i, pagina in enumerate(reader.pages, start=1):
    texto = pagina.extract_text() or ""
    texto_completo.append(f"\n--- Página {i} ---\n{texto}")

full = "\n".join(texto_completo)
print(full[:3000])  # preview

# Guardar a .md para que Copilot lo lea en otra conversación
Path("contrato-proveedor.md").write_text(full, encoding="utf-8")

# Opción B: pdfplumber — mejor para tablas
import pdfplumber
with pdfplumber.open(ARCHIVO) as pdf:
    for i, page in enumerate(pdf.pages, start=1):
        for j, tabla in enumerate(page.extract_tables()):
            print(f"\n=== Tabla pág. {i} #{j+1} ===")
            for fila in tabla:
                print(" | ".join((c or "").strip() for c in fila))
```

**Si el PDF es escaneado** (no se extrae texto):
```python
# OCR — solo si pypdf devolvió vacío
from pdf2image import convert_from_path
import pytesseract
# pytesseract requiere instalar Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
imagenes = convert_from_path(ARCHIVO, dpi=200)
texto = "\n".join(pytesseract.image_to_string(img, lang="spa+eng") for img in imagenes)
```

**Qué siempre buscar en un PDF de negocio**:
- **SLAs / penalidades** en contratos.
- **Fechas críticas** (vencimientos, hitos, revisiones).
- **Owners / firmantes** (nombres y cargos).
- **Cifras monetarias** y unidades (¿USD o MXN? ¿con o sin IVA?).

## Después de la extracción: el análisis

Estructura tu respuesta al usuario siempre así:

```
## TL;DR
[3 líneas máximo]

## Datos clave extraídos
| Campo | Valor |
|---|---|
| ... | ... |

## Hallazgos / Riesgos
- 🔴 ...
- 🟡 ...
- 🟢 ...

## Preguntas abiertas
- ¿...?
- ¿...?

## Próximos pasos sugeridos
1. ...
2. ¿Quieres que genere [Excel/PPTX/correo]?
```

## Notas

- **Privacidad**: si el archivo trae datos personales (correos, salarios, nombres de clientes), recuérdale al usuario que esté consciente de qué modelo está usando. Modelos en la nube ven el contenido.
- **Archivos grandes**: para Excel/PDF >50MB, procesa por chunks o por hoja/página individual, no cargues todo en memoria.
- **Archivos protegidos con contraseña**: `openpyxl` y `pypdf` lo soportan con `password=`. Pídele la contraseña al usuario por terminal, **no la hardcodees**.
- **Versionado**: si el usuario va a analizar el mismo archivo recurrentemente (ej. reporte semanal), sugiere guardar el script en `scripts/analizar-XYZ.py` para reutilizarlo.
- **No alucines cifras**: si una celda dice `#REF!`, `#N/A` o está vacía, repórtalo tal cual; no inventes valores.
