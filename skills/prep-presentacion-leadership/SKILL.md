---
name: prep-presentacion-leadership
description: "Prepara una presentación con leadership (VP, C-level, board, steering committee): anticipa preguntas afiladas, define 3 talking points anclados, identifica qué NO decir, mapea trampas políticas y diseña respaldo de datos. Para gerentes de desarrollo y product managers que presentan roadmaps, QBRs, headcount requests, post-incident reviews o propuestas de inversión."
---

# Prep para presentación con leadership

## Propósito

Presentar a leadership no es presentar a tu equipo. Tienen menos tiempo, menos contexto, más preguntas afiladas y otra agenda. Esta skill te prepara para sobrevivir, comunicar con claridad y salir bien parado.

## Audiencia

- **Gerentes de desarrollo**: presentar progreso técnico, retos de infra, propuestas de inversión en plataforma, headcount requests, post-mortem de incidentes a C-level.
- **Product managers**: presentar roadmap, resultados de iniciativas, business case de nueva línea de producto, kill/grow decisions, alineación de prioridades con sales/marketing.

## Cuándo usarla

- QBR / review trimestral con VP/Director.
- Pitch de iniciativa o headcount request.
- Update de proyecto crítico al staff/board.
- Conversación post-incidente con C-level.
- Steering committee cross-funcional.
- "Te quieren ver mañana 30 min" (estos son los más peligrosos).

## Instrucciones

1. **Pregunta primero** (críticas):
   - ¿Audiencia exacta? (nombres, roles, qué le importa a CADA UNO).
   - ¿Cuánto tiempo total? ¿Cuánto presentar vs Q&A?
   - ¿Cuál es el OBJETIVO específico? (decisión, alineación, información).
   - ¿Hay una decisión específica que necesitas que tomen?
   - ¿Hay temas sensibles políticos? (otras áreas afectadas, presupuesto reasignado).
   - ¿Tienen contexto previo o llegas en frío?
   - ¿Quién más en la sala podría objetar y por qué?

2. **Construye el "memo previo"** (máximo 1 página, antes del deck):
   - **TL;DR de 3 líneas**: qué, por qué, qué necesitas.
   - **Decisión solicitada**: 1 frase. (Si no hay decisión, dilo: "Solo informativo").
   - **Backup**: 3-5 datos clave que sostienen tu argumento.

3. **Anticipa las 10 preguntas más probables** y prepara respuestas de 2 líneas:
   - "¿Cuánto cuesta?" (siempre la primera).
   - "¿Qué pasa si NO lo hacemos?"
   - "¿Cómo se compara con X competidor / industria?"
   - "¿Por qué tú/tu equipo y no [otra área]?"
   - "¿Cómo medimos éxito?"
   - "¿Qué riesgos no estás contemplando?"
   - "¿Por qué ahora?"
   - "¿Se puede hacer con menos / más rápido?"
   - "¿Quién más está alineado?"
   - "¿Cuándo veo resultados?"

4. **Identifica las "trampas"**:
   - **Tema que NO quieres profundizar** y por qué (ej. métrica que bajó, falla reciente).
   - **Pregunta que te va a doler** (la del fundador que sabe demasiado, la del CFO que conoce los números).
   - **Persona que probablemente objete** y su agenda real.

5. **3 talking points anclados** (las 3 frases a las que SIEMPRE regresas):
   - **Mensaje principal**: ____ (lo único que recordarán mañana).
   - **Dato más fuerte**: ____ (el número que sostiene todo).
   - **Resultado deseado**: ____ (la decisión que pides).

   Si te desvían, regresa siempre a estas 3.

6. **Salida**: markdown estructurado. Si el usuario quiere el deck real, encadena con `generar-presentacion-pptx`.

## Plantilla de salida

```markdown
# Prep: [Tema] con [Audiencia] — [Fecha]

## Contexto
- **Audiencia**: [nombres y roles, qué le importa a cada uno]
- **Tiempo**: [X min total, Y presentando, Z Q&A]
- **Objetivo**: [decisión / alineación / informativo]
- **Decisión solicitada**: [1 frase, o "ninguna"]

## TL;DR del memo (lo que dirías en el elevador)
1. [Qué]
2. [Por qué importa ahora]
3. [Qué necesito de ustedes]

## 3 talking points anclados
- **Mensaje principal**: ...
- **Dato más fuerte**: ...
- **Resultado deseado**: ...

## Las 10 preguntas que me van a hacer

| # | Pregunta | Respuesta de 2 líneas | Dato/fuente para respaldar |
|---|---|---|---|
| 1 | ¿Cuánto cuesta? | ... | ... |
| 2 | ¿Qué pasa si no lo hacemos? | ... | ... |
| 3 | ¿Cómo se compara con competidor X? | ... | ... |
| 4 | ¿Por qué tú? | ... | ... |
| 5 | ¿Cómo medimos éxito? | ... | ... |
| 6 | ¿Qué riesgos no contemplas? | ... | ... |
| 7 | ¿Por qué ahora? | ... | ... |
| 8 | ¿Se puede hacer con menos? | ... | ... |
| 9 | ¿Quién más está alineado? | ... | ... |
| 10 | ¿Cuándo veo resultados? | ... | ... |

## Trampas a manejar
- **Tema que NO quiero profundizar**: [qué] — Si preguntan, redirijo con: "[frase puente]"
- **Pregunta que más me duele**: [pregunta] — Plan: [reconocer + redirigir]
- **Persona que probablemente objete**: [nombre] — Su preocupación real es: [...] — Mi respuesta: [...]

## Qué NO decir
- No prometer fechas sin buffer (siempre +30%).
- No comparar negativamente con otras áreas.
- No usar jerga técnica innecesaria.
- No improvisar números (di "te lo confirmo por escrito" si dudas).
- No echar culpas (ni siquiera disfrazadas).
- No decir "deberíamos" — sí "propongo".

## Mi propia preparación
- [ ] Imprimir 1 copia del memo + 1 copia del backup.
- [ ] Probar tecnología 15 min antes (proyector, audio, demo).
- [ ] Llegar 10 min antes para small talk informal con la audiencia.
- [ ] Hidratarme. NO café en exceso.
- [ ] Tener listo el "next step" para cerrar fuerte.

## Plan B
- Si se acaba el tiempo: ¿qué slide es prescindible? → [slide N]
- Si me bajan de la agenda: ¿cuál es la versión email de 5 líneas? → [...]
- Si la respuesta es "no": ¿qué pido como consolación? (ej. revisión en 30 días).
```

## Casos especiales

### Headcount request
- Lleva siempre el costo de NO contratar (deuda técnica, oportunidad perdida, burnout, churn).
- Ten lista la JD del rol y el plan de onboarding (muestra que ya pensaste el siguiente paso).

### Post-incident con C-level
- Lidera con impacto y acciones (no con timeline).
- Cultura blameless en lenguaje, pero ownership claro en acciones.
- Ten métricas de prevención: "lo que estamos cambiando para que no vuelva a pasar".

### Roadmap a board (PMs)
- 1 slide de visión, 1 de progreso, 1 de próximas apuestas, 1 de riesgos.
- Conecta cada bet a un OKR / business outcome — no a features.
- Anticipa la pregunta "¿qué estamos dejando de hacer?".

## Anti-patterns a evitar

- Llegar con 40 slides para 20 minutos.
- Leer el slide en lugar de hablar.
- Defender en lugar de escuchar la objeción.
- Improvisar números delante del CFO. Nunca.
- Asumir que conocen el contexto de tu equipo.
- "Estamos trabajando duro" — sin números no significa nada.

## Notas

- **Antes de la presentación**: pide 15 min con tu jefe para correrle el deck. Suele ahorrarte un golpe en vivo.
- **Tema sensible**: alinea antes 1:1 con el VP. Nunca lo enteres en grupo.
- **Después**: envía email de follow-up dentro de 24h con resumen + acuerdos + dueños.
- **Si te dicen "decide tú"**: agradece, decide, y comunica la decisión por email para que conste.
