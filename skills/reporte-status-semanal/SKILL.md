---
name: reporte-status-semanal
description: "Genera el reporte de status semanal de un equipo (logros, en progreso, riesgos, ayudas necesarias, métricas) en formato consistente listo para enviar a leadership o stakeholders. Para gerentes de desarrollo y product managers que envían update semanal. Usa cuando el usuario pida 'mi status del viernes', un update para su jefe, o un resumen de sprint."
---

# Reporte de status semanal

## Propósito

Estandarizar el "viernes de status" para que tu jefe vea siempre el mismo formato. Reduce tiempo de redacción y aumenta credibilidad ("ya sé qué buscar en este reporte").

## Audiencia

- **Gerentes de desarrollo**: update semanal a VP de Ingeniería, métricas de delivery, riesgos técnicos.
- **Product managers**: update a Head of Product / VP, progreso de roadmap, señales de mercado, dependencies con engineering.

## Cuándo usarla

- Update semanal a tu jefe directo.
- Resumen al cierre de sprint.
- Update a stakeholders cross-funcionales (sales, support, marketing).
- Reporte mensual condensado a partir de 4 semanales.

## Instrucciones

1. **Pregunta primero**:
   - ¿Qué pasó esta semana? (logros, hitos, lanzamientos)
   - ¿Qué está en progreso? (con % o ETA)
   - ¿Qué se quedó atrás y por qué?
   - ¿Qué riesgos hay para la próxima semana?
   - ¿Necesitas algo de tu jefe? (decisión, recurso, escalation, air cover)
   - ¿Métricas relevantes? (DORA, NPS, velocity, $$ revenue, adopción)
   - ¿Audiencia? (¿técnica o de negocio?)

2. **Formato fijo** (no cambiar entre semanas — la consistencia es el valor):
   - **TL;DR** (3 líneas máximo, lo que tu jefe leerá si solo tiene 30 segundos).
   - **Logros de la semana** (3-5 bullets, con impacto cuantificado).
   - **En progreso** (3-5 bullets, con % y owner).
   - **Riesgos & banderas rojas** (🔴🟡🟢 con mitigación).
   - **Ayuda necesaria** (decisiones, recursos, escalations).
   - **Métricas** (tabla pequeña, comparada vs. semana anterior).
   - **La semana próxima** (3 prioridades).

3. **Tono**: directo, sin adornos. Nada de "estamos trabajando duro" — sí "deployamos 14 PRs, resolvimos 3 bugs P1, abrimos 2 incidentes (ambos mitigados <30min)".

4. **Salida**: markdown listo para pegar en Outlook/Slack/Teams. Si el usuario lo pide en Excel o Word, encadena con `generar-reporte-excel`.

## Plantilla

```markdown
# Status semanal — [Equipo / Producto] — Sem [N] (DD-MMM al DD-MMM)

## TL;DR
- [Hito principal de la semana]
- [Riesgo principal]
- [Decisión que necesito]

## Logros 🏆
- [Logro 1 con número/impacto] — *Owner*
- [Logro 2] — *Owner*
- ...

## En progreso 🚧
- [Iniciativa 1] — [%] — Owner: [nombre] — ETA: [fecha]
- ...

## Riesgos 🚦
| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| 🔴 ... | Alta | Alto | ... |
| 🟡 ... | Media | Medio | ... |

## Ayuda necesaria 🙋
- [ ] **Decisión**: ¿X o Y? — Necesito por: [fecha]
- [ ] **Recurso**: ...
- [ ] **Escalation**: ...

## Métricas 📊
| Métrica | Esta sem | Sem pasada | Δ |
|---|---|---|---|
| ... | ... | ... | ▲/▼ |

## Próxima semana 🎯
1. ...
2. ...
3. ...
```

## Variantes por audiencia

- **A tu jefe directo (VP Eng / Head of Product)**: incluye métricas técnicas y de equipo (people).
- **A C-level / staff**: condensa al TL;DR + riesgos + ayuda. Máximo 1 pantalla.
- **A stakeholders cross-funcionales**: enfatiza dependencies, ETAs externos, lo que necesitas de ellos.

## Anti-patterns a evitar

- Cambiar formato cada semana (rompe la utilidad de consistencia).
- "Más es mejor": 1 página máximo. Si necesitas más, separa en doc anexo.
- Marcar todo verde: si todo está verde nadie te cree. Si todo está rojo, no estás filtrando.
- Pedir ayuda sin specificar QUÉ necesitas y para CUÁNDO.

## Notas

- Si tu jefe quiere otro formato, adáptalo y úsalo como plantilla nueva — pero NO mezcles formatos.
- Encadena con `metricas-dora` si quieres profundizar en métricas de delivery.
- Encadena con `generar-reporte-excel` o `generar-presentacion-pptx` para el resumen mensual/trimestral.
- Guarda los status pasados en una carpeta — sirven para construir tu review trimestral.
