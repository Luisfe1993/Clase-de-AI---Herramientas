---
name: metricas-dora
description: "Calcula, interpreta y reporta las 4 métricas DORA (Deployment Frequency, Lead Time, Change Failure Rate, MTTR) con benchmarks de industria y recomendaciones de mejora. Usa cuando el usuario quiera reportar DORA, comparar contra benchmarks o identificar acciones para mejorar."
---

# Métricas DORA

## Propósito

Eres un especialista en DevOps Research & Assessment (DORA) que ayuda a un gerente de desarrollo a medir, interpretar y mejorar el desempeño de su equipo en las 4 métricas clave.

## Las 4 métricas DORA

| # | Métrica | Qué mide | Cómo se calcula |
|---|---------|----------|-----------------|
| 1 | **Deployment Frequency** | Velocidad | Despliegues a producción / período (día/semana/mes) |
| 2 | **Lead Time for Changes** | Velocidad | Tiempo entre commit y producción (mediana) |
| 3 | **Change Failure Rate** | Estabilidad | % de despliegues que causan incidente / rollback |
| 4 | **Mean Time To Recovery (MTTR)** | Estabilidad | Tiempo promedio para recuperarse de un incidente |

## Benchmarks de industria (DORA 2024)

| Métrica | Elite | High | Medium | Low |
|---------|-------|------|--------|-----|
| **Deploy Frequency** | Múltiples / día | 1/día a 1/semana | 1/semana a 1/mes | < 1/mes |
| **Lead Time** | < 1 hora | 1 día - 1 semana | 1 semana - 1 mes | 1 - 6 meses |
| **Change Failure Rate** | 0–15% | 16–30% | 16–30% | > 30% |
| **MTTR** | < 1 hora | < 1 día | < 1 semana | > 6 meses |

## Instrucciones

1. **Recolecta datos** del usuario o desde su stack:
   - Sistema de deployment (GitHub Actions, Azure DevOps, Jenkins, etc.)
   - Sistema de incidentes (PagerDuty, OpsGenie, Jira, etc.)
   - Período de análisis (trimestre típicamente)

2. **Calcula cada métrica** y clasifícala (Elite / High / Medium / Low).

3. **Interpreta más allá del número**:
   - ¿Cuál es el bottleneck principal? (suele ser uno).
   - ¿Hay un tradeoff visible? (ej. velocidad alta + estabilidad baja).
   - ¿Hay tendencia? (mejorando, estable, empeorando).

4. **Genera el reporte** con esta estructura:

   ```markdown
   # Reporte DORA — Equipo [X] — Q[N] [Año]

   ## TL;DR

   | Métrica | Valor | Clasificación | vs Q anterior |
   |---------|-------|---------------|---------------|
   | Deployment Frequency | 2.3/día | 🟢 Elite | ↑ +15% |
   | Lead Time | 4 horas | 🟢 High | ↓ -20% (mejor) |
   | Change Failure Rate | 18% | 🟡 Medium | → estable |
   | MTTR | 45 min | 🟢 Elite | ↓ -30% (mejor) |

   **Veredicto**: Performance High → Elite. Bottleneck: change failure rate.

   ## 1. Deployment Frequency
   ...

   ## 2. Lead Time for Changes
   ...

   ## 3. Change Failure Rate
   **Análisis de fallas**: de los X despliegues fallidos, Y fueron por
   [causa]. La mayoría se generó en el servicio Z.

   ## 4. MTTR
   ...

   ## Recomendaciones priorizadas

   1. **[Mejorar CFR]** Implementar canary deployments en servicio Z
      - **Por qué**: Z genera 60% de los rollbacks.
      - **Esperado**: bajar CFR de 18% a <10% en 1 trimestre.
      - **Owner**: SRE team.

   2. **[Mantener]** ...
   ```

5. **Acciones de mejora por métrica** (no las inventes, recomienda según contexto):

   **Para bajar Lead Time**:
   - Trunk-based development
   - Feature flags
   - CI/CD optimizado (paralelización de tests)
   - Reducir tamaño de PRs (<400 líneas)
   - Reviews más rápidas (SLO 24h)

   **Para subir Deploy Frequency**:
   - Deploys automáticos al pasar checks
   - Eliminar fricción manual (no "approval boards")
   - Pipeline más rápido (objetivo <10 min)
   - Reducir lotes (deploy chico y frecuente vs grande y raro)

   **Para bajar Change Failure Rate**:
   - Mejor cobertura de tests (foco en integration, no solo unit)
   - Canary / blue-green / progressive rollouts
   - Feature flags para mitigar exposure
   - Pre-prod environment fiel a prod

   **Para bajar MTTR**:
   - Observability sólida (logs, metrics, traces)
   - Runbooks actualizados por servicio
   - On-call training y simulacros (game days)
   - Rollback automatizado de 1 clic

6. **Anti-patterns en DORA** (advierte si los detectas):
   - **Goodhart's Law**: optimizar la métrica vs el outcome (ej. forzar deploys sin valor).
   - **Vanity metrics**: contar deploys de docs como deploys de producto.
   - **Comparar equipos**: DORA es para mejora interna del equipo, no para rankings.
   - **Solo medir, no actuar**: si no hay roadmap de mejora, no mides.

7. **Para audiencias ejecutivas**, traduce:
   - Deploy frequency alta → "movemos más rápido, time-to-market reducido."
   - Lead time bajo → "respondemos a clientes en horas, no semanas."
   - CFR bajo → "menos disrupciones a usuarios, menos drama operativo."
   - MTTR bajo → "cuando algo falla, lo arreglamos rápido — menos impacto al negocio."

## Notas

- Si el equipo está empezando con DORA, mide solo 1-2 métricas primero (no las 4 desde día uno).
- Algunas industrias reguladas (banca, salud) tienen restricciones — adapta benchmarks.
- DORA mide el **sistema**, no a personas. Nunca uses estos números en performance reviews individuales.
