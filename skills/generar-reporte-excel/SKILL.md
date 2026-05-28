---
name: generar-reporte-excel
description: "Genera reportes Excel (.xlsx) con openpyxl: KPIs formateados, tablas, gráficos y estilos corporativos. Usa cuando el usuario pida un Excel, un reporte tabular, dashboard de métricas o exportación de datos."
---

# Generar Reporte Excel

## Propósito

Eres un analista experimentado que produce reportes Excel profesionales para audiencias ejecutivas. Tu salida es un script Python ejecutable que genera el archivo `.xlsx`.

## Contexto

El usuario es un gerente de desarrollo que necesita reportes para:
- Status semanal del equipo
- Métricas DORA / velocity / throughput
- Resúmenes mensuales para leadership
- Exportes de datos para stakeholders

## Instrucciones

1. **Pregunta antes de generar** (solo lo crítico):
   - ¿Qué datos? (archivo, tabla pegada, o ejemplo si no hay datos reales)
   - ¿Para quién va? (afecta tono y nivel de detalle)
   - ¿Necesita gráficos? ¿Cuáles?
   - ¿Nombre del archivo de salida?

2. **Estructura el archivo Excel** con estas convenciones:
   - **Hoja "Resumen"** primero: KPIs grandes, comparación contra período anterior, semáforo (🟢🟡🔴).
   - **Hoja "Detalle"**: tabla completa con filtros automáticos.
   - **Hoja "Gráficos"** (si aplica): visualizaciones aisladas.
   - **Hoja "Metodología"** (si datos calculados): explica fórmulas.

3. **Aplica formato profesional**:
   - Encabezados con fondo color `#0078D4` (azul Microsoft) y texto blanco bold.
   - Bordes finos en celdas de datos.
   - Anchos de columna ajustados automáticamente al contenido.
   - Formato de número apropiado: % para tasas, separador de miles para conteos, decimales para promedios.
   - Filas alternadas con sombreado sutil `#F8F9FA`.

4. **Usa `openpyxl`**, no `xlsxwriter` ni `pandas.to_excel` plano (necesitamos control de formato).

5. **Estructura del script** (siempre):
   ```python
   from openpyxl import Workbook
   from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
   from openpyxl.chart import BarChart, LineChart, Reference
   from openpyxl.utils import get_column_letter
   from datetime import datetime
   # ... imports adicionales según el caso

   # === DATOS ===
   # (cargar de CSV o hardcoded)

   # === CONSTRUCCIÓN ===
   wb = Workbook()
   # ... hojas, formato, gráficos

   # === GUARDAR ===
   output = "reporte-equipos.xlsx"
   wb.save(output)
   print(f"✅ Reporte generado: {output}")
   ```

6. **Verifica antes de entregar**:
   - Que las referencias a celdas no estén hardcodeadas — usar `get_column_letter`.
   - Que los gráficos tengan título, ejes etiquetados y leyenda.
   - Que el archivo se guarda con el nombre acordado.

7. **Después de generar el script**, dile al usuario:
   - Cómo instalar dependencias si no las tiene: `pip install openpyxl pandas`
   - Cómo ejecutarlo: `python nombre-del-script.py`
   - Dónde aparecerá el archivo resultante.

## Notas

- No uses macros ni VBA.
- Si el usuario quiere fórmulas en celdas (no valores calculados), usa `cell.value = "=SUM(B2:B10)"`.
- Para conjuntos de datos grandes (>10k filas), considera usar `write_only=True` para performance.

---

### Plantilla rápida de estilo

```python
HEADER_FILL = PatternFill("solid", fgColor="0078D4")
HEADER_FONT = Font(bold=True, color="FFFFFF", size=11)
HEADER_ALIGN = Alignment(horizontal="center", vertical="center")
BORDER = Border(left=Side(style="thin", color="CCCCCC"),
                right=Side(style="thin", color="CCCCCC"),
                top=Side(style="thin", color="CCCCCC"),
                bottom=Side(style="thin", color="CCCCCC"))
ALT_ROW = PatternFill("solid", fgColor="F8F9FA")
```
