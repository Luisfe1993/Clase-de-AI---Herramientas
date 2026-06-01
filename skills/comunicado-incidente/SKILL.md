---
name: comunicado-incidente
description: "Genera comunicaciones durante un incidente productivo: status page público, email a clientes afectados, mensaje a leadership interno y update en canal de respuesta. Para gerentes de desarrollo y product managers liderando o coordinando un incidente. Usa cuando haya un outage, degradación de servicio, brecha de seguridad o bug crítico que requiera comunicación rápida y coordinada."
---

# Comunicado de incidente

## Propósito

Durante un incidente productivo cada minuto cuenta. Esta skill produce, en paralelo, las 3-4 comunicaciones que típicamente se necesitan — con tono apropiado para cada audiencia y formato listo para pegar.

## Audiencia

- **Gerentes de desarrollo**: lideran respuesta técnica y comunican con leadership e ingeniería.
- **Product managers**: comunican con clientes, support, marketing y áreas de negocio impactadas.

## Cuándo usarla

- Outage productivo (parcial o total).
- Degradación de servicio que afecta SLAs.
- Brecha de seguridad (involucra legal en paralelo).
- Bug crítico que requiere rollback público.

## Instrucciones

1. **Pregunta primero** (rápido — el reloj corre):
   - ¿Qué pasó? (1-2 líneas)
   - ¿Desde cuándo? ¿Sigue activo o ya está mitigado?
   - ¿Quiénes están afectados? (% de usuarios, regiones, planes)
   - ¿ETA de resolución conservador? (no inventar)
   - ¿Hay workaround para el usuario?
   - Severidad (P0 / P1 / P2)
   - ¿A qué canales se publica? (status page, email, Slack interno, prensa)

2. **Genera 4 versiones** (siempre, salvo que el usuario diga lo contrario):
   - **Status page (público)**: tono neutro, factual, sin culpar.
   - **Email a clientes afectados**: empático, claro sobre impacto y siguientes pasos.
   - **Mensaje a leadership interno**: directo, con números, ETA y riesgo de negocio.
   - **Update en canal de respuesta**: técnico, para el equipo mitigando.

3. **Reglas de tono no negociables**:
   - Nunca uses "Estamos trabajando en ello" sin especificar QUÉ se está haciendo.
   - Nunca prometas ETAs que no puedas cumplir. Mejor "actualizaremos en 30 min" que "estará resuelto en 1h".
   - No asignes culpa pública. La cultura blameless empieza por el comunicado.
   - Para brechas de seguridad: usa "estamos investigando" hasta tener confirmación.

4. **Cada comunicado debe incluir**:
   - Título/asunto específico (no "Issue" — sí "Pagos con tarjeta no procesan desde 10:30am").
   - Primera línea: qué pasa, desde cuándo, qué hace el usuario.
   - Cuerpo: impacto, workaround si hay.
   - Pie: cuándo es el próximo update.

## Plantillas

### Status page (público)

```text
[INVESTIGANDO | IDENTIFICADO | MONITOREANDO | RESUELTO]
[Servicio]: [descripción breve del impacto]

A las [HH:MM ZONA] detectamos [qué]. Los usuarios pueden experimentar [síntoma].

[Workaround si aplica]

Estamos trabajando en [acción específica]. Próximo update: [HH:MM].
```

### Email a clientes afectados

```text
Asunto: [Acción] [Servicio] - [Estado]

Hola [Nombre],

Queremos informarte que entre las [HH:MM] y las [HH:MM] del [fecha] el servicio [X] presentó [problema]. Esto afectó tu capacidad de [qué].

Qué pasó: [explicación clara, sin jerga]
Impacto en ti: [específico al cliente]
Qué hicimos: [acción concreta]
Qué sigue: [próximos pasos, créditos si aplica]

Lamentamos la inconveniencia. Si tienes preguntas, responde este correo o contacta support@[...].

[Tu nombre y rol]
```

### Mensaje a leadership

```text
[P0/P1/P2] [Servicio] [Activo/Mitigado/Resuelto]

Qué: [1 línea]
Desde: [HH:MM] | Duración: [X min]
Impacto: [% usuarios | $ revenue at risk | clientes enterprise específicos]
Causa probable: [hipótesis si se conoce]
Mitigación: [acción en curso]
ETA resolución: [conservador]
Riesgo escalation: [comunicación pública? legal? SLA breach?]

Próximo update: [HH:MM]
```

### Update en canal de respuesta interno

```text
[HH:MM] Update IR-2026-XXX
Status: [investigando/mitigando/monitoreando]
Hipótesis actual: ...
En proceso: [nombre] está [acción]
Pendiente: ...
Próximo sync: [HH:MM]
```

## Después del incidente

Recomienda al usuario encadenar con `postmortem-incidente` una vez resuelto (idealmente dentro de 5 días hábiles).

## Notas

- **Cumplimiento legal**: para brechas de seguridad en jurisdicciones reguladas (GDPR, LFPDPPP, HIPAA) hay plazos legales de notificación (72h GDPR). Pregunta antes de redactar.
- **Status page silenciosa es peor que ninguna**. Mejor "investigando" cada 30 min que silencio.
- **Lenguaje localizado**: si tu base de clientes es bilingüe, genera versión ES y EN.
- **Una sola voz**: define un único portavoz por canal. Comunicaciones contradictorias generan más crisis.
