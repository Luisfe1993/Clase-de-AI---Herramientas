# Sprint 20 — Equipo Plataforma — Datos de ejemplo

> Estos son datos ficticios para practicar con la skill `retro-equipo`.

## Información general

- **Duración**: 2 semanas (del 6 al 20 de mayo de 2026)
- **Equipo**: 6 ingenieros (1 staff, 2 senior, 2 mid, 1 junior) + 1 PM + 1 designer
- **Sprint goal**: Migrar el servicio de autenticación a OAuth 2.1 y desplegar canary del rediseño del checkout.

## Capacidad

- Capacidad teórica: 54 puntos
- Capacidad real (post PTO y on-call): 48 puntos
- **Comprometido**: 50 puntos ⚠️ (un poco sobre-compromiso)

## Resultado

- **Entregado**: 42 puntos de 50 (84%)
- **Carry-over al sprint 21**: 8 puntos (Story de feature flags)

## Eventos relevantes del sprint

- **Día 3**: Incidente P2 en producción — login falló para 12% de usuarios por 35 min.
  Causa raíz: race condition en el flow nuevo de OAuth.
  Acción inmediata: rollback. Postmortem programado.

- **Día 5**: Juan (junior) hizo su primer deploy a producción 🎉.

- **Día 8**: Reunión de planning trimestral interrumpió 2 horas el día de focus time del equipo.

- **Día 10**: Ana (senior) trajo un PR de 850 líneas. Review tomó 3 días en cerrarse. Equipo frustrado.

- **Día 12**: Carlos (staff) hizo pair programming con María (mid) para desbloquear la story de canary deploy. Excelente colaboración.

- **Día 14**: Demo a stakeholders salió bien. PM marketing está emocionado.

## Métricas DORA del sprint

| Métrica | Valor | Clasificación |
|---------|-------|---------------|
| Deployments a prod | 8 | High |
| Lead time promedio | 7.5 hrs | High |
| Change failure rate | 12.5% (1 de 8) | Elite |
| MTTR | 35 min | Elite |

## Pulso del equipo (encuesta anónima fin de sprint)

| Pregunta | Promedio (1-5) |
|----------|----------------|
| Mi carga de trabajo fue manejable | 3.2 ⚠️ |
| Tengo claridad sobre prioridades | 4.5 |
| Recibo apoyo cuando me atoro | 4.0 |
| El sprint goal era alcanzable | 3.5 ⚠️ |
| Tuve focus time suficiente | 2.8 ❌ |

## Temas que aparecieron en comentarios

- "Demasiadas reuniones esta quincena."
- "PRs grandes nos están frenando."
- "Bueno que Carlos hizo pair con María."
- "El incidente nos asustó pero lo manejamos bien."
- "¿Podemos automatizar más el on-call playbook?"

---

## 💡 Cómo usar esto

Abre el chat de GitHub Copilot y pídele:

> Usando la skill `retro-equipo`, diseña una retrospectiva para este sprint. El archivo `ejemplos/sprint-historico.md` tiene todos los datos. Recomienda un marco apropiado y prepárame la agenda y las preguntas guía.
