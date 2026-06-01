"""
Genera archivos de ejemplo para practicar la skill `analizar-archivos-existentes`:
- presupuesto-q2.xlsx  -> Excel con varias hojas, totales y banderas rojas
- review-q1.pptx       -> Deck con KPIs, tabla de riesgos y notas del orador
- contrato-proveedor.pdf -> PDF con SLAs, penalidades, fechas y firmantes

Ejecutar una sola vez:
    python ejemplos/_generar-ejemplos.py
"""
from pathlib import Path
from datetime import date

OUT = Path(__file__).parent


# =========================================================
# 1) EXCEL: presupuesto-q2.xlsx
# =========================================================
def crear_excel():
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter

    AZUL = PatternFill("solid", fgColor="0078D4")
    ALT = PatternFill("solid", fgColor="F8F9FA")
    ROJO = PatternFill("solid", fgColor="F8D7DA")
    HEADER_FONT = Font(bold=True, color="FFFFFF", size=11)
    BOLD = Font(bold=True)
    BORDER = Border(
        left=Side(style="thin", color="CCCCCC"),
        right=Side(style="thin", color="CCCCCC"),
        top=Side(style="thin", color="CCCCCC"),
        bottom=Side(style="thin", color="CCCCCC"),
    )
    CENTER = Alignment(horizontal="center", vertical="center")

    wb = Workbook()

    # --- Hoja Resumen ---
    ws = wb.active
    ws.title = "Resumen"
    ws["A1"] = "Presupuesto Q2 2026 — Plataforma Digital"
    ws["A1"].font = Font(bold=True, size=14, color="0078D4")
    ws.merge_cells("A1:D1")

    ws["A3"] = "Concepto"
    ws["B3"] = "Asignado (USD)"
    ws["C3"] = "Gastado (USD)"
    ws["D3"] = "Disponible (USD)"
    for c in ("A3", "B3", "C3", "D3"):
        ws[c].fill = AZUL
        ws[c].font = HEADER_FONT
        ws[c].alignment = CENTER
        ws[c].border = BORDER

    resumen = [
        ("Personal (headcount)", 480000, 462000),
        ("Infraestructura cloud", 95000, 118500),   # sobregirada
        ("Licencias SaaS", 60000, 41200),
        ("Capacitación", 25000, 8500),
        ("Contingencia", 20000, 0),
    ]
    for i, (concepto, asignado, gastado) in enumerate(resumen, start=4):
        ws.cell(row=i, column=1, value=concepto).border = BORDER
        ws.cell(row=i, column=2, value=asignado).border = BORDER
        ws.cell(row=i, column=3, value=gastado).border = BORDER
        # Fórmula real
        ws.cell(row=i, column=4, value=f"=B{i}-C{i}").border = BORDER
        if i % 2 == 0:
            for col in range(1, 5):
                ws.cell(row=i, column=col).fill = ALT
        # Bandera roja si gastado > asignado
        if gastado > asignado:
            for col in range(1, 5):
                ws.cell(row=i, column=col).fill = ROJO

    # Totales — total disponible HARDCODED MAL a propósito (bandera roja para el análisis)
    total_row = 4 + len(resumen)
    ws.cell(row=total_row, column=1, value="TOTAL").font = BOLD
    ws.cell(row=total_row, column=2, value=f"=SUM(B4:B{total_row-1})").font = BOLD
    ws.cell(row=total_row, column=3, value=f"=SUM(C4:C{total_row-1})").font = BOLD
    # ⚠️ INTENCIONAL: el "disponible total" está hardcoded y no cuadra con asignado-gastado.
    ws.cell(row=total_row, column=4, value=58000).font = BOLD  # debería ser 49,800
    for col in range(1, 5):
        ws.cell(row=total_row, column=col).border = BORDER

    # Formato de moneda
    for row in range(4, total_row + 1):
        for col in range(2, 5):
            ws.cell(row=row, column=col).number_format = '"$"#,##0'

    # Anchos
    ws.column_dimensions["A"].width = 30
    for col in ("B", "C", "D"):
        ws.column_dimensions[col].width = 18

    ws["A12"] = "Nota: revisar con CFO antes del 30-jun-2026"
    ws["A12"].font = Font(italic=True, color="666666")

    # --- Hoja Detalle ---
    ws2 = wb.create_sheet("Detalle gastos")
    headers = ["Fecha", "Categoría", "Proveedor", "Descripción", "Monto (USD)", "Aprobado por"]
    for col, h in enumerate(headers, start=1):
        c = ws2.cell(row=1, column=col, value=h)
        c.fill = AZUL
        c.font = HEADER_FONT
        c.alignment = CENTER
        c.border = BORDER

    detalle = [
        ("2026-04-02", "Infraestructura cloud", "Azure", "Reserved instances DB", 28500, "L. Sandé"),
        ("2026-04-15", "Personal", "Nómina abril", "Salarios 12 ing.", 154000, "RRHH"),
        ("2026-04-22", "Licencias SaaS", "Datadog", "Renovación anual", 18000, "L. Sandé"),
        ("2026-05-03", "Infraestructura cloud", "Azure", "Egress traffic overage", 21000, "L. Sandé"),
        ("2026-05-10", "Capacitación", "Udemy Business", "Plan equipo", 8500, "L. Sandé"),
        ("2026-05-18", "Personal", "Nómina mayo", "Salarios 12 ing.", 154000, "RRHH"),
        ("2026-05-25", "Infraestructura cloud", "Azure", "OpenAI tokens premium", 38000, ""),  # sin aprobador
        ("2026-05-30", "Licencias SaaS", "GitHub Copilot", "Renovación 25 asientos", 23200, "L. Sandé"),
        ("2026-06-01", "Personal", "Nómina junio (parcial)", "Salarios 12 ing.", 154000, "RRHH"),
    ]
    for i, row in enumerate(detalle, start=2):
        for col, val in enumerate(row, start=1):
            c = ws2.cell(row=i, column=col, value=val)
            c.border = BORDER
            if col == 5:
                c.number_format = '"$"#,##0'
        if i % 2 == 0:
            for col in range(1, len(headers) + 1):
                ws2.cell(row=i, column=col).fill = ALT
    # Auto-filter
    ws2.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{len(detalle) + 1}"
    for col, w in enumerate([12, 22, 18, 30, 14, 16], start=1):
        ws2.column_dimensions[get_column_letter(col)].width = w

    # --- Hoja oculta (a propósito) ---
    ws3 = wb.create_sheet("_ajustes_internos")
    ws3["A1"] = "Ajustes contables Q1 (no compartir)"
    ws3["A2"] = "Reclasificación gasto OpenAI -> opex extraordinario"
    ws3["A3"] = "Monto: $12,500"
    ws3.sheet_state = "hidden"

    salida = OUT / "presupuesto-q2.xlsx"
    wb.save(salida)
    print(f"OK Excel:  {salida}")


# =========================================================
# 2) POWERPOINT: review-q1.pptx
# =========================================================
def crear_pptx():
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.enum.text import PP_ALIGN

    AZUL = RGBColor(0x00, 0x78, 0xD4)
    GRIS = RGBColor(0x32, 0x31, 0x30)
    BLANCO = RGBColor(0xFF, 0xFF, 0xFF)
    VERDE = RGBColor(0x10, 0x7C, 0x10)
    ROJO = RGBColor(0xC4, 0x32, 0x4E)

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    BLANK = prs.slide_layouts[6]

    # --- Portada ---
    s = prs.slides.add_slide(BLANK)
    banda = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(2))
    banda.fill.solid()
    banda.fill.fore_color.rgb = AZUL
    banda.line.fill.background()

    tb = s.shapes.add_textbox(Inches(0.7), Inches(0.55), Inches(12), Inches(1.4))
    tb.text_frame.text = "Review Q1 2026"
    p = tb.text_frame.paragraphs[0]
    p.font.size = Pt(44); p.font.bold = True; p.font.color.rgb = BLANCO

    tb2 = s.shapes.add_textbox(Inches(0.7), Inches(2.4), Inches(12), Inches(1))
    tb2.text_frame.text = "Equipo Plataforma Digital · Enero–Marzo 2026"
    tb2.text_frame.paragraphs[0].font.size = Pt(22)
    tb2.text_frame.paragraphs[0].font.color.rgb = GRIS

    tb3 = s.shapes.add_textbox(Inches(0.7), Inches(6.2), Inches(12), Inches(0.6))
    tb3.text_frame.text = "Luis Sandé · Gerente de Desarrollo · Abril 2026"
    tb3.text_frame.paragraphs[0].font.size = Pt(14)
    tb3.text_frame.paragraphs[0].font.color.rgb = GRIS

    s.notes_slide.notes_text_frame.text = (
        "Audiencia: VP de Producto + Director de Ingeniería. Tiempo: 20 min + Q&A."
    )

    # --- KPIs ---
    s = prs.slides.add_slide(BLANK)
    titulo = s.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(12), Inches(0.8))
    titulo.text_frame.text = "KPIs del trimestre"
    titulo.text_frame.paragraphs[0].font.size = Pt(32)
    titulo.text_frame.paragraphs[0].font.bold = True
    titulo.text_frame.paragraphs[0].font.color.rgb = AZUL

    kpis = [
        ("Deployment Frequency", "12 / sem", "▲ 33% vs Q4", VERDE),
        ("Lead Time for Changes", "2.4 días", "▼ 18% vs Q4", VERDE),
        ("Change Failure Rate", "9.5%", "▲ 2 pp vs Q4", ROJO),
        ("MTTR", "47 min", "▼ 12% vs Q4", VERDE),
    ]
    for i, (label, valor, delta, color) in enumerate(kpis):
        left = Inches(0.6 + i * 3.1)
        top = Inches(2)
        w = Inches(2.9); h = Inches(2.5)
        box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, w, h)
        box.fill.solid(); box.fill.fore_color.rgb = BLANCO
        box.line.color.rgb = AZUL
        tf = box.text_frame
        tf.text = valor
        tf.paragraphs[0].alignment = PP_ALIGN.CENTER
        tf.paragraphs[0].font.size = Pt(36)
        tf.paragraphs[0].font.bold = True
        tf.paragraphs[0].font.color.rgb = AZUL
        p = tf.add_paragraph(); p.text = label
        p.alignment = PP_ALIGN.CENTER
        p.font.size = Pt(13); p.font.color.rgb = GRIS
        p2 = tf.add_paragraph(); p2.text = delta
        p2.alignment = PP_ALIGN.CENTER
        p2.font.size = Pt(12); p2.font.bold = True; p2.font.color.rgb = color

    s.notes_slide.notes_text_frame.text = (
        "Cuidado al presentar el CFR de 9.5%: subió por el incidente del 14-feb (rollback de auth). "
        "Si preguntan, mencionar que el postmortem ya cerró todas las acciones correctivas."
    )

    # --- Logros ---
    s = prs.slides.add_slide(BLANK)
    tb = s.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(12), Inches(0.8))
    tb.text_frame.text = "Logros del trimestre"
    tb.text_frame.paragraphs[0].font.size = Pt(32); tb.text_frame.paragraphs[0].font.bold = True
    tb.text_frame.paragraphs[0].font.color.rgb = AZUL

    body = s.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(12), Inches(5))
    bullets = [
        "Migración de autenticación a OAuth 2.1: 100% del tráfico migrado en 6 semanas (planeado 10).",
        "Reducción de costos cloud: -22% en S3 al implementar lifecycle policies.",
        "Onboarding: 3 nuevos ingenieros productivos en <30 días gracias al runbook actualizado.",
        "Pipeline de CI/CD: tiempo promedio bajó de 14 min a 6 min tras paralelizar tests.",
        "Cobertura de tests: pasó de 62% a 78% en los repos core.",
    ]
    for i, t in enumerate(bullets):
        if i == 0:
            body.text_frame.text = "• " + t
            body.text_frame.paragraphs[0].font.size = Pt(18)
            body.text_frame.paragraphs[0].font.color.rgb = GRIS
        else:
            p = body.text_frame.add_paragraph()
            p.text = "• " + t
            p.font.size = Pt(18); p.font.color.rgb = GRIS
            p.space_before = Pt(8)

    s.notes_slide.notes_text_frame.text = "Pedir a Ana que prepare el dato exacto de ahorro en S3 (USD)."

    # --- Riesgos (tabla) ---
    s = prs.slides.add_slide(BLANK)
    tb = s.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(12), Inches(0.8))
    tb.text_frame.text = "Riesgos identificados"
    tb.text_frame.paragraphs[0].font.size = Pt(32); tb.text_frame.paragraphs[0].font.bold = True
    tb.text_frame.paragraphs[0].font.color.rgb = AZUL

    riesgos = [
        ["Riesgo", "Impacto", "Mitigación"],
        ["Dependencia vendor pagos (un solo proveedor)", "Alto", "POC con 2do proveedor en Q2"],
        ["Burnout en equipo de SRE (rotación 2/6)", "Alto", "Contratar 1 SRE + redistribuir on-call"],
        ["Deuda técnica en módulo de reportes", "Medio", "Reservar 20% del Q2 para refactor"],
        ["Costos OpenAI crecieron 3x", "Medio", "Cache de prompts + modelo más barato para baja prioridad"],
    ]
    rows, cols = len(riesgos), len(riesgos[0])
    tabla = s.shapes.add_table(rows, cols, Inches(0.6), Inches(1.5), Inches(12), Inches(4.5)).table
    for c_idx, header in enumerate(riesgos[0]):
        cell = tabla.cell(0, c_idx)
        cell.text = header
        cell.fill.solid(); cell.fill.fore_color.rgb = AZUL
        for p in cell.text_frame.paragraphs:
            p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = BLANCO
    for r_idx, row in enumerate(riesgos[1:], start=1):
        for c_idx, val in enumerate(row):
            cell = tabla.cell(r_idx, c_idx)
            cell.text = val
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(12); p.font.color.rgb = GRIS

    s.notes_slide.notes_text_frame.text = (
        "El riesgo de burnout es el más urgente. Si VP pregunta, ya hay req aprobado para 1 SRE adicional."
    )

    # --- Próximos pasos ---
    s = prs.slides.add_slide(BLANK)
    tb = s.shapes.add_textbox(Inches(0.6), Inches(0.4), Inches(12), Inches(0.8))
    tb.text_frame.text = "Próximos pasos Q2"
    tb.text_frame.paragraphs[0].font.size = Pt(32); tb.text_frame.paragraphs[0].font.bold = True
    tb.text_frame.paragraphs[0].font.color.rgb = AZUL

    body = s.shapes.add_textbox(Inches(0.8), Inches(1.4), Inches(12), Inches(5))
    pasos = [
        ("Cerrar POC vendor de pagos", "L. Sandé", "30-may"),
        ("Onboarding SRE nuevo", "Ana M.", "15-jun"),
        ("Refactor módulo reportes (fase 1)", "Carlos R.", "30-jun"),
        ("Cache de prompts OpenAI", "Diego T.", "15-jun"),
    ]
    for i, (qué, owner, fecha) in enumerate(pasos):
        linea = f"• {qué}  —  Owner: {owner}  —  Fecha: {fecha}"
        if i == 0:
            body.text_frame.text = linea
            body.text_frame.paragraphs[0].font.size = Pt(18)
            body.text_frame.paragraphs[0].font.color.rgb = GRIS
        else:
            p = body.text_frame.add_paragraph()
            p.text = linea
            p.font.size = Pt(18); p.font.color.rgb = GRIS
            p.space_before = Pt(10)

    s.notes_slide.notes_text_frame.text = "Pedir compromiso explícito de VP en el req del SRE antes de fin de mes."

    salida = OUT / "review-q1.pptx"
    prs.save(salida)
    print(f"OK PPTX:   {salida}")


# =========================================================
# 3) PDF: contrato-proveedor.pdf
# =========================================================
def crear_pdf():
    from reportlab.lib.pagesizes import LETTER
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    )
    from reportlab.lib.enums import TA_LEFT, TA_CENTER

    salida = OUT / "contrato-proveedor.pdf"
    doc = SimpleDocTemplate(
        str(salida), pagesize=LETTER,
        leftMargin=0.9 * inch, rightMargin=0.9 * inch,
        topMargin=0.9 * inch, bottomMargin=0.9 * inch,
        title="Contrato MSA — CloudNova SA",
    )

    styles = getSampleStyleSheet()
    H1 = ParagraphStyle("H1", parent=styles["Heading1"], textColor=colors.HexColor("#0078D4"))
    H2 = ParagraphStyle("H2", parent=styles["Heading2"], textColor=colors.HexColor("#0078D4"))
    BODY = styles["BodyText"]
    BODY.alignment = TA_LEFT
    BODY.fontSize = 10.5
    BODY.leading = 14

    story = []

    story.append(Paragraph("Contrato Marco de Servicios (MSA)", H1))
    story.append(Paragraph(
        "Entre <b>CloudNova SA de CV</b> (\"Proveedor\") y "
        "<b>Plataforma Digital Holdings</b> (\"Cliente\")", BODY))
    story.append(Spacer(1, 0.2 * inch))

    metadata = [
        ["Número de contrato", "MSA-2026-0418"],
        ["Fecha de firma", "18 de abril de 2026"],
        ["Vigencia", "12 meses (renovación automática)"],
        ["Fecha de renovación", "18 de abril de 2027"],
        ["Moneda", "USD (sin IVA, IVA aplicable al 16%)"],
    ]
    t = Table(metadata, colWidths=[2.2 * inch, 3.8 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#F3F2F1")),
        ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#323130")),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.3 * inch))

    # --- Cláusula 1: objeto ---
    story.append(Paragraph("1. Objeto del contrato", H2))
    story.append(Paragraph(
        "El Proveedor prestará servicios de hospedaje en nube administrada, "
        "monitoreo 24/7 y soporte técnico nivel L2/L3 para los ambientes "
        "productivos del Cliente, conforme a los niveles de servicio establecidos "
        "en la sección 3.", BODY))
    story.append(Spacer(1, 0.15 * inch))

    # --- Cláusula 2: precio ---
    story.append(Paragraph("2. Contraprestación", H2))
    story.append(Paragraph(
        "El Cliente pagará una cuota mensual fija de <b>USD $48,500.00</b> "
        "más consumo variable. La facturación se emite el día 5 de cada mes "
        "con vencimiento a 30 días naturales.", BODY))
    story.append(Spacer(1, 0.15 * inch))

    # --- Cláusula 3: SLAs ---
    story.append(Paragraph("3. Niveles de servicio (SLA)", H2))
    sla_data = [
        ["Métrica", "Compromiso", "Penalidad por incumplimiento"],
        ["Uptime mensual", "99.95%", "5% crédito mensual por cada 0.1% por debajo"],
        ["Tiempo de respuesta crítico (P1)", "≤ 15 min", "10% crédito mensual si se supera 3 veces/mes"],
        ["Tiempo de respuesta alto (P2)", "≤ 1 hora", "5% crédito mensual si se supera 5 veces/mes"],
        ["Tiempo de resolución crítico (P1)", "≤ 4 horas", "15% crédito mensual si se supera 1 vez/mes"],
        ["Reporte mensual de servicio", "Día 10 hábil", "USD $500 por día de retraso"],
    ]
    sla_table = Table(sla_data, colWidths=[2 * inch, 1.5 * inch, 3.2 * inch])
    sla_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0078D4")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#CCCCCC")),
        ("FONTSIZE", (0, 0), (-1, -1), 9.5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8F9FA")]),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(sla_table)
    story.append(Spacer(1, 0.15 * inch))
    story.append(Paragraph(
        "<i>El crédito total por mes no podrá exceder el 25% de la cuota mensual fija.</i>", BODY))

    story.append(PageBreak())

    # --- Cláusula 4: terminación ---
    story.append(Paragraph("4. Terminación anticipada", H2))
    story.append(Paragraph(
        "Cualquiera de las partes podrá terminar el contrato con un aviso por "
        "escrito de <b>90 días naturales</b>. En caso de terminación por causa "
        "imputable al Proveedor (incumplimiento sostenido de SLA por 3 meses "
        "consecutivos), el aviso será de <b>30 días</b> y sin penalidad para el Cliente.", BODY))
    story.append(Paragraph(
        "Si el Cliente termina anticipadamente sin causa, pagará una penalidad "
        "equivalente al <b>20% del valor remanente</b> del contrato.", BODY))
    story.append(Spacer(1, 0.15 * inch))

    # --- Cláusula 5: confidencialidad ---
    story.append(Paragraph("5. Confidencialidad y datos personales", H2))
    story.append(Paragraph(
        "El Proveedor se obliga a tratar toda la información del Cliente como "
        "confidencial por un plazo de <b>5 años</b> posteriores a la terminación. "
        "El tratamiento de datos personales se rige por la LFPDPPP y por el "
        "Anexo Técnico de Protección de Datos.", BODY))
    story.append(Spacer(1, 0.15 * inch))

    # --- Cláusula 6: límite de responsabilidad ---
    story.append(Paragraph("6. Límite de responsabilidad", H2))
    story.append(Paragraph(
        "La responsabilidad total del Proveedor frente al Cliente, por cualquier "
        "causa, no excederá el equivalente a <b>12 meses</b> de la cuota mensual "
        "fija pagada en los 12 meses anteriores al evento.", BODY))
    story.append(Spacer(1, 0.3 * inch))

    # --- Firmas ---
    story.append(Paragraph("Firmas", H2))
    firmas = [
        ["Por el Cliente", "Por el Proveedor"],
        ["", ""],
        ["___________________________", "___________________________"],
        ["Luis Sandé", "María Fernanda Estrada"],
        ["Gerente de Desarrollo", "Director Comercial"],
        ["Plataforma Digital Holdings", "CloudNova SA de CV"],
        ["Fecha: 18-abr-2026", "Fecha: 18-abr-2026"],
    ]
    ft = Table(firmas, colWidths=[3.3 * inch, 3.3 * inch])
    ft.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 30),  # espacio para firma
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ]))
    story.append(ft)

    doc.build(story)
    print(f"OK PDF:    {salida}")


if __name__ == "__main__":
    crear_excel()
    crear_pptx()
    crear_pdf()
    print("\nListo. Tres archivos generados en ejemplos/")
