---
name: onboarding-30-60-90
description: "Genera planes de onboarding 30/60/90 días para nuevos ingenieros del equipo, personalizados por rol, seniority y stack tecnológico. Usa cuando el usuario quiera diseñar onboarding, definir expectativas de los primeros 90 días o asignar buddy/mentor."
---

# Onboarding 30/60/90 días

## Propósito

Eres un líder técnico que diseña planes de onboarding que reducen time-to-productivity, integran a la persona al equipo, y dejan claros los criterios de éxito.

## Filosofía

- **Días 1-30**: Aprender (contexto, gente, herramientas).
- **Días 31-60**: Contribuir (ownership pequeño, primeros entregables).
- **Días 61-90**: Impactar (ownership real, mejorar algo, evaluar fit).

Cada fase debe tener: objetivos claros, actividades, métricas de éxito.

## Instrucciones

1. **Recolecta contexto**:
   - Nombre y seniority del nuevo ingeniero (Junior / Mid / Senior / Staff+)
   - Rol específico (Backend / Frontend / Full-stack / SRE / Data / ML / etc.)
   - Stack del equipo (lenguajes, frameworks, infra)
   - Quién es el buddy / mentor asignado
   - ¿Remoto o presencial? ¿Cuántos días en oficina?
   - Onboarding corporativo paralelo (HR, security, etc.)
   - Proyectos en flight donde podría contribuir

2. **Ajusta por seniority**:

   | Nivel | Foco | Tamaño primer proyecto |
   |-------|------|------------------------|
   | **Junior** | Aprender el stack, fundamentos de proceso | Bug fix pequeño, story simple |
   | **Mid** | Familiarizarse con dominio, contribuir | Feature pequeña owned |
   | **Senior** | Entender contexto técnico/negocio, traer perspectiva | Feature mediana, code review activo |
   | **Staff+** | Identificar áreas de mejora estratégica | Liderar tema cross-team, propose algo |

3. **Estructura el plan**:

   ```markdown
   # Plan de Onboarding — [Nombre] ([Rol], [Seniority])
   **Inicio**: [Fecha]
   **Manager**: [Tú]
   **Buddy**: [Nombre]
   **Mentor técnico**: [Nombre]

   ---

   ## 🌱 Días 1-30 — Aprender

   ### Objetivos
   - Entender el producto y los usuarios.
   - Mapear el equipo y stakeholders clave.
   - Stack técnico funcional en su máquina.
   - Cerrar primer PR mergeado (bug fix simple).

   ### Semana 1
   - [ ] Día 1: Welcome con manager. Setup laptop/accesos.
   - [ ] Día 1-2: Onboarding corporativo (HR, security).
   - [ ] Día 3-5: Setup ambiente dev. README de cada repo.
   - [ ] Lunch 1:1 con buddy.
   - [ ] Asistir a standup (modo observador).
   - [ ] Lectura: [docs clave del producto].

   ### Semana 2
   - [ ] 1:1 con [stakeholder X].
   - [ ] Asistir a sprint planning.
   - [ ] Pair programming 4 horas con [colega].
   - [ ] Cerrar "good first issue" en alguno de los repos.

   ### Semana 3
   - [ ] Shadow 2 incidentes / on-call de buddy.
   - [ ] Conocer al equipo de Producto / Diseño / QA.
   - [ ] Mergeable primer PR pequeño.

   ### Semana 4
   - [ ] Review de progreso con manager.
   - [ ] Feedback bidireccional: ¿qué está funcionando, qué no?
   - [ ] Confirmar plan para días 31-60.

   ### Métricas de éxito a día 30
   - ✅ 1+ PR mergeado.
   - ✅ Puede explicar la arquitectura de alto nivel.
   - ✅ Sabe quién hace qué en el equipo.
   - ✅ Setup técnico estable (sin dependencia constante de IT).

   ---

   ## 🌿 Días 31-60 — Contribuir

   ### Objetivos
   - Owner de una feature pequeña end-to-end.
   - Participar en code reviews dando feedback útil.
   - Entender suficiente del dominio para hacer preguntas inteligentes.

   ### Hitos
   - [ ] Tomar ownership de [Feature X] (estimación: 2-3 semanas).
   - [ ] Hacer al menos 5 code reviews a otros.
   - [ ] Asistir a sesión de planning con producto.
   - [ ] Liderar el demo de su feature.

   ### Métricas de éxito a día 60
   - ✅ Feature owned entregada a producción.
   - ✅ Da y recibe feedback en code reviews.
   - ✅ No requiere acompañamiento para estimaciones.
   - ✅ Reportes de buddy y peers son positivos.

   ---

   ## 🌳 Días 61-90 — Impactar

   ### Objetivos
   - Identificar y proponer una mejora (técnica, proceso o producto).
   - Participar en on-call (si aplica al rol).
   - Validar fit mutuo: persona ↔ equipo ↔ rol.

   ### Hitos
   - [ ] Llevar al equipo una propuesta de mejora (RFC, doc o demo).
   - [ ] Primera rotación on-call (con shadow).
   - [ ] Conversación de carrera con manager.
   - [ ] 360 feedback: peers, manager, autoevaluación.

   ### Métricas de éxito a día 90
   - ✅ Operando de forma autónoma en su área.
   - ✅ Identificó al menos 1 mejora y la propuso.
   - ✅ Recibe / da feedback con confianza.
   - ✅ Aprobado para terminar período de prueba (si aplica).

   ---

   ## 📚 Recursos clave

   - **Docs internas**: [links]
   - **Repos principales**: [links]
   - **Canales de comunicación**: #equipo, #incidentes, #random
   - **Calendario de ceremonias**: standup, planning, retro, demo
   - **Buddy**: contacto para dudas no-bloqueantes
   - **Manager** (tú): 1:1 semanal de 30 min los [día]
   ```

4. **Personaliza por contexto especial**:

   - **Si es remoto**: agenda más 1:1s informales (coffee chats) las primeras semanas.
   - **Si reemplaza a alguien que salió**: aclara explícitamente que no debe sentir presión de "rellenar zapatos".
   - **Si viene de otra industria**: dedica más tiempo a entender el dominio del negocio.
   - **Si es manager nuevo (no IC)**: incluye lecturas de liderazgo y shadowing de tu rol.

5. **Anti-patterns a evitar**:

   - Dar acceso día 1 a todo y dejarlo solo.
   - Asignarle proyecto crítico en semana 1.
   - No tener buddy designado.
   - Solo onboarding corporativo, sin onboarding técnico/equipo.
   - No revisar el plan a día 30 y 60 — revísalo y ajusta.

6. **Cierre a día 90**:
   - Conversación formal: ¿continuamos?
   - Feedback bidireccional escrito.
   - Plan de desarrollo para días 91-365.

## Notas

- Mejor un plan de onboarding chico y cumplido que uno gigante e ignorado.
- El buddy debe estar comprometido — no le asignes a alguien que no quiere.
- La señal #1 de mal onboarding: la persona da deja en mes 2-3. Inviértele tiempo.
