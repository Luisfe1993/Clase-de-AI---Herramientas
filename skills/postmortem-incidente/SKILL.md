---
name: postmortem-incidente
description: "Estructura un postmortem REAL después de un incidente productivo: timeline, root cause analysis (5 Whys / Ishikawa), contributing factors, action items SMART y cultura blameless. NO confundir con la skill 'postmortem' (que es pre-mortem de planes futuros). Para gerentes de desarrollo y product managers responsables de la review de incidentes."
---

# Postmortem de incidente

## Propósito

Convertir un incidente doloroso en aprendizaje organizacional. El postmortem NO es para asignar culpa — es para que ese incidente específico no vuelva a pasar.

## Diferencia con la skill `postmortem`

- `postmortem` (skill global): **pre-mortem** — analiza un plan FUTURO asumiendo que ya falló para encontrar riesgos.
- `postmortem-incidente` (esta): análisis de un evento PASADO real para extraer aprendizajes y acciones.

## Audiencia

- **Gerentes de desarrollo**: lideran el postmortem, garantizan la cultura blameless, dueños de action items técnicos.
- **Product managers**: aportan impacto en clientes/negocio, alinean prioridad de action items vs. roadmap, comunican a stakeholders.

## Cuándo usarla

- Incidentes P0/P1 (siempre).
- P2 si hay patrón recurrente.
- Después de cualquier rollback público.
- Después de cualquier evento que afecte SLA o tenga comunicación a clientes.

## Instrucciones

1. **Pregunta primero**:
   - ID del incidente y fecha
   - Severidad
   - Duración (inicio → mitigación → resolución total)
   - Servicios afectados
   - Quiénes participaron en la respuesta
   - ¿Tienes ya el timeline crudo? (logs, Slack, status page)
   - ¿Hubo comunicación pública? (status page, email, prensa)

2. **Construye el documento** con esta estructura fija:

   1. **Resumen ejecutivo** (10 líneas máximo — lo que leerán los VPs).
   2. **Impacto cuantificado**: usuarios afectados, % tráfico, $ revenue, SLA breach, daño reputacional.
   3. **Timeline** (con UTC y zona local, minuto a minuto desde el primer síntoma):
      - HH:MM — Qué pasó (objetivo)
      - HH:MM — Qué hizo el equipo (decisión)
   4. **Análisis de causa raíz** (5 Whys o Ishikawa):
      - Causa directa
      - Causas contribuyentes
      - Por qué los safeguards no funcionaron
   5. **Lo que funcionó** (no solo lo malo — qué nos salvó).
   6. **Lo que no funcionó** (gaps de detección, runbooks faltantes, alertas mal configuradas).
   7. **Action items** (SMART, con owner y fecha):
      - Inmediato (esta semana): parches, alertas.
      - Corto plazo (este mes): runbooks, testing.
      - Largo plazo (este trimestre): cambios arquitectónicos.
   8. **Lecciones para la organización** (qué generaliza a otros equipos).

3. **Cultura blameless** (no negociable):
   - Nunca uses nombres en "qué salió mal" — usa roles ("el on-call recibió la alerta a las 03:15").
   - Asume buenas intenciones. Cualquier humano en esa situación habría hecho lo mismo.
   - Pregunta "qué del sistema permitió este error" no "quién cometió este error".
   - Si alguien sintió que falló: refuerza que el sistema falló, no la persona.

4. **Action items que sí se cierran**:
   - SMART: Specific, Measurable, Assignable, Realistic, Time-bound.
   - Máximo 5-7 action items totales. Más = ninguno se cierra.
   - Cada uno con dueño NOMBRADO y fecha en calendario.
   - Review en 30 días para ver % de cierre.

5. **Salida**: markdown estructurado, listo para Confluence/Notion/Wiki. Si el usuario quiere PPTX para presentar en review de incidentes con leadership, encadena con `generar-presentacion-pptx`.

## Plantilla completa

```markdown
# Postmortem: [Título descriptivo] — [Fecha]

**ID**: IR-2026-XXX | **Severidad**: P0 | **Duración**: Xh Ym | **Status**: Resuelto
**Autores**: [nombres] | **Reviewers**: [nombres]

## Resumen ejecutivo
[10 líneas máximo: qué pasó, impacto, causa raíz, qué cambia]

## Impacto
- Usuarios afectados: X (Y% del total)
- Revenue impactado: $X estimado
- SLA: [breach / no breach] — crédito esperado: $X
- Reputacional: [tickets de support, menciones en redes, churn signals]
- Comunicación pública: [sí/no, qué se dijo]

## Timeline (CDT / UTC)

| Hora | Evento |
|---|---|
| 10:30 / 16:30 | Primer error 500 en endpoint /pay. Sin alerta. |
| 10:42 / 16:42 | Cliente Foo abre ticket P1. |
| 10:48 / 16:48 | On-call recibe page. |
| 11:05 / 17:05 | Rollback iniciado del PR #4521. |
| 11:18 / 17:18 | Servicio recuperado. Monitoreando. |
| 11:50 / 17:50 | Incidente cerrado. |

## Causa raíz

**Causa directa**: PR #4521 cambió el schema de `payments.amount` de int a decimal sin migración compatible. Las queries de lectura fallaron con type mismatch.

**Por qué llegó a producción** (5 Whys):
1. ¿Por qué no lo detectó CI? → No hay tests de integración para queries de pago.
2. ¿Por qué no hubo canary? → Sí hubo, pero no recibió tráfico de pagos (bug en routing).
3. ¿Por qué no alertó? → La métrica `payment_success_rate` bajaba, pero el threshold era 95% y bajamos a 92%.
4. ¿Por qué el threshold estaba en 95%? → Heredado de hace 2 años, nunca revisado.
5. ¿Por qué no se revisaba? → No hay proceso de review periódico de thresholds.

**Causas contribuyentes**:
- Documentación de migración de schemas desactualizada.
- On-call no tenía runbook para "fallas de pago".
- Deploy en viernes a las 10am (proceso lo permitía).

## Lo que funcionó ✅
- Detección por cliente fue rápida (12 min después del deploy).
- Rollback fue limpio (sin pérdida de datos).
- Comunicación a leadership clara (template de `comunicado-incidente`).

## Lo que no funcionó ❌
- Detección automática (no hubo alerta).
- Canary no validó tráfico crítico.
- On-call no sabía a quién escalar.

## Action items

### Inmediato (esta semana)
- [ ] [SRE] Ajustar threshold de `payment_success_rate` a 98%. **Owner**: Ana M. **Fecha**: 03-jun.
- [ ] [Eng] Test de integración para queries de pago. **Owner**: Carlos R. **Fecha**: 05-jun.

### Corto plazo (este mes)
- [ ] Runbook "Fallas de pago" en wiki. **Owner**: Diego T. **Fecha**: 30-jun.
- [ ] Fix de routing del canary para incluir tráfico de pagos. **Owner**: Ana M. **Fecha**: 15-jun.
- [ ] Proceso de review trimestral de thresholds. **Owner**: Manager SRE. **Fecha**: 30-jun.

### Largo plazo (este trimestre)
- [ ] Migración a schema evolution con backward compatibility automática. **Owner**: TBD. **Fecha**: fin Q3.

## Lecciones para la organización
- Cualquier cambio a schemas de tablas críticas debe pasar por checklist de compatibilidad.
- Los canarys deben validar mix de tráfico de los flujos críticos, no solo "tráfico genérico".
- Thresholds de alertas deben revisarse trimestralmente.

## Anexos
- Logs relevantes: [link]
- Slack thread del incidente: [link]
- PR causante: [link]
- Comunicado público: [link]
```

## Notas

- El postmortem debe redactarse **dentro de los 5 días hábiles** post-resolución.
- Comparte un draft con los responsables ANTES de publicar — no es para sorprender a nadie.
- Si hay implicaciones legales/regulatorias, involucra legal antes de circular.
- Review de action items a los 30 días: si <50% cerrados, escala. Si <20% cerrados, el postmortem fue teatro.
- Publica los postmortems internamente. Esconderlos mata la cultura blameless.
