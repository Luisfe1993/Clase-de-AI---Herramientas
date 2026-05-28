---
name: generar-presentacion-pptx
description: "Genera presentaciones PowerPoint (.pptx) ejecutivas con python-pptx: portada, KPIs, bullets, tablas, charts y branding corporativo. Usa cuando el usuario pida un PowerPoint, una presentación, un deck o slides."
---

# Generar Presentación PowerPoint

## Propósito

Produces decks de calidad ejecutiva listos para audiencias de leadership. Tu salida es un script Python ejecutable con `python-pptx`.

## Contexto

Un gerente de desarrollo necesita decks frecuentemente:
- Reviews trimestrales (QBRs)
- Updates de roadmap a leadership
- Postmortems / incident reports
- Propuestas de iniciativas
- All-hands del equipo

## Instrucciones

1. **Pregunta primero**:
   - Título y audiencia
   - Duración aproximada (15 min ≈ 8-10 slides; 30 min ≈ 15-20)
   - ¿Tienen plantilla corporativa o usamos estilo neutro Microsoft?
   - Datos clave a incluir
   - ¿Hay reporte Excel previo del que extraer KPIs?

2. **Estructura narrativa** (úsala como default y ajusta):
   1. **Portada** — Título, subtítulo (alcance/período), nombre del presentador, fecha.
   2. **Agenda** — 3-5 puntos de qué van a ver.
   3. **Contexto / Situación actual** — Resumen ejecutivo.
   4. **KPIs principales** — Slide tipo dashboard con 4 cuadros grandes.
   5. **Logros** — Bullets concretos con métricas.
   6. **Retos / Riesgos** — Tabla con riesgo, impacto, mitigación.
   7. **Próximos pasos** — Plan concreto con owners y fechas.
   8. **Cierre** — Llamado a la acción / preguntas.

3. **Estilo visual**:
   - Paleta: azul Microsoft `#0078D4`, gris oscuro `#323130` para texto, blanco para fondos.
   - Fuente: **Segoe UI** (default de Microsoft).
   - Tamaños: títulos 32-36pt, subtítulos 24pt, body 18pt, captions 12pt.
   - Máximo 5 bullets por slide; cada bullet máximo 1 línea idealmente.
   - Evita texto denso — usa un slide por idea.

4. **Usa `python-pptx`** con esta estructura base:

   ```python
   from pptx import Presentation
   from pptx.util import Inches, Pt, Emu
   from pptx.dml.color import RGBColor
   from pptx.enum.shapes import MSO_SHAPE
   from pptx.enum.text import PP_ALIGN
   from datetime import datetime

   # Colores corporativos
   AZUL = RGBColor(0x00, 0x78, 0xD4)
   GRIS_OSCURO = RGBColor(0x32, 0x31, 0x30)
   GRIS_CLARO = RGBColor(0xF3, 0xF2, 0xF1)
   BLANCO = RGBColor(0xFF, 0xFF, 0xFF)

   prs = Presentation()
   prs.slide_width = Inches(13.333)   # widescreen
   prs.slide_height = Inches(7.5)

   # ... slides

   prs.save("review-trimestral.pptx")
   ```

5. **Patrones reutilizables**:

   **KPI Card** (cuadro con número grande):
   ```python
   def kpi_card(slide, left, top, width, height, valor, etiqueta, delta=None):
       box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
       box.fill.solid()
       box.fill.fore_color.rgb = BLANCO
       box.line.color.rgb = AZUL
       tf = box.text_frame
       tf.text = valor
       tf.paragraphs[0].font.size = Pt(48)
       tf.paragraphs[0].font.bold = True
       tf.paragraphs[0].font.color.rgb = AZUL
       p = tf.add_paragraph()
       p.text = etiqueta
       p.font.size = Pt(14)
       p.font.color.rgb = GRIS_OSCURO
       if delta:
           p2 = tf.add_paragraph()
           p2.text = delta
           p2.font.size = Pt(12)
           p2.font.color.rgb = RGBColor(0x10, 0x7C, 0x10) if delta.startswith("▲") else RGBColor(0xC4, 0x32, 0x4E)
   ```

   **Slide de título de sección**:
   ```python
   def slide_seccion(prs, titulo):
       slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
       # banda azul a la izquierda
       banda = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.5), prs.slide_height)
       banda.fill.solid()
       banda.fill.fore_color.rgb = AZUL
       banda.line.fill.background()
       # título
       tb = slide.shapes.add_textbox(Inches(1), Inches(3), Inches(11), Inches(1.5))
       tb.text_frame.text = titulo
       tb.text_frame.paragraphs[0].font.size = Pt(40)
       tb.text_frame.paragraphs[0].font.bold = True
       tb.text_frame.paragraphs[0].font.color.rgb = GRIS_OSCURO
       return slide
   ```

6. **Tras generar el script**, instruye al usuario:
   - Instalar: `pip install python-pptx`
   - Ejecutar: `python nombre-del-script.py`
   - El `.pptx` se abre con doble clic en PowerPoint o Keynote.

7. **Si el usuario lo va a presentar en remoto**, recuerda:
   - Tamaño de fuente mínimo 18pt para que se lea en video.
   - Alto contraste (texto oscuro sobre fondo claro).
   - No usar gráficos con leyendas microscópicas.

## Notas

- Si el usuario pide gráficos complejos, considera generarlos primero con `matplotlib` y embed como imagen.
- Para imágenes ya disponibles, usa `slide.shapes.add_picture(path, left, top, width)`.
- Si necesitas notas del presentador: `slide.notes_slide.notes_text_frame.text = "..."`.
