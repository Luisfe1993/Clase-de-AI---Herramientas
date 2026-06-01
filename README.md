# Clase de AI — Herramientas para Gerentes de Desarrollo y Product Managers

> Curso práctico en español para aprender a usar **VS Code + GitHub Copilot Chat + Modelos de AI** como herramienta diaria de un gerente de desarrollo o product manager.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F%20%2B%20Copilot-blue)](https://github.com/features/copilot)

---

## 🎯 ¿Qué vas a aprender?

Al terminar la clase serás capaz de:

1. **Instalar** y configurar VS Code, Git y GitHub Copilot.
2. **Usar** el chat de GitHub Copilot dentro de VS Code (modo Ask, Edit y Agent).
3. **Cambiar** entre modelos de AI (GPT-5, Claude Sonnet, Gemini, etc.).
4. **Descargar** repositorios públicos de GitHub y usarlos como base.
5. **Crear** tus propias *skills* y *agentes* personalizados en español.
6. **Generar** reportes en Excel y presentaciones en PowerPoint con prompts.
7. **Analizar** archivos que ya tienes (Excel, PowerPoint y PDF) para extraer insights accionables.
8. **Aplicar** todo esto a casos reales de gestión: sprints, retros, 1:1s, métricas DORA, code review, onboarding, incidentes productivos, status semanales, conversaciones difíciles y presentaciones a leadership.

---

## 🧭 Antes de la clase

Sigue el archivo **[PRE-CLASE-INSTALACION.md](PRE-CLASE-INSTALACION.md)** unos días antes para llegar con todo instalado y la cuenta de GitHub Copilot activa.

> 💡 Si no alcanzas a instalar todo, no te preocupes — el primer módulo del curso cubre la instalación paso a paso.

---

## 📚 Contenido del repositorio

```
Clase-de-AI---Herramientas/
├── README.md                     ← Estás aquí
├── PRE-CLASE-INSTALACION.md      ← Lee esto antes de la clase
├── curso/
│   └── index.html                ← 🎓 Curso interactivo (abre en tu navegador)
├── skills/                       ← Skills personalizadas en español (14)
│   ├── generar-reporte-excel/
│   ├── generar-presentacion-pptx/
│   ├── analizar-archivos-existentes/
│   ├── plan-sprint/
│   ├── retro-equipo/
│   ├── prep-one-on-one/
│   ├── revisar-pr/
│   ├── metricas-dora/
│   ├── onboarding-30-60-90/
│   ├── comunicado-incidente/         ← Comunicar un outage productivo
│   ├── reporte-status-semanal/       ← Status semanal a leadership / stakeholders
│   ├── postmortem-incidente/         ← Postmortem REAL post-incidente (NO pre-mortem)
│   ├── conversacion-dificil/         ← Feedback, despido, decisión impopular (SBI)
│   └── prep-presentacion-leadership/ ← QBR, headcount, roadmap, post-incident
├── skills-globales/              ← Skills extra más generales (en inglés)
│   ├── postmortem/                  Pre-mortem brutal de un plan
│   ├── analysis-report-authoring/   Reporte analítico multi-audiencia
│   ├── ba-automated-analysis/       Análisis automatizado de Power BI (MCP)
│   └── data-definitions-dictionary/ Diccionario de columnas de un dataset
├── agents/
│   └── gerente-desarrollo.chatmode.md   ← Modo agente personalizado
├── ejemplos/
│   ├── metricas-equipo.csv       ← Dataset CSV para Excel
│   ├── sprint-historico.md       ← Datos para retros
│   ├── presupuesto-q2.xlsx       ← Excel para practicar análisis
│   ├── review-q1.pptx            ← Deck para practicar análisis
│   ├── contrato-proveedor.pdf    ← PDF para practicar análisis
│   └── _generar-ejemplos.py      ← Script que regenera los 3 archivos anteriores
└── .github/
    └── copilot-instructions.md   ← Instrucciones globales para Copilot
```

---

## 🚀 Cómo empezar (3 pasos)

1. **Descarga este repo**: clic en el botón verde **Code** → **Download ZIP** (o usa `git clone`).
2. **Abre el curso**: doble clic en `curso/index.html` para abrirlo en tu navegador.
3. **Abre el workspace en VS Code**: **doble clic en `Clase-de-AI.code-workspace`** (o desde VS Code: `Archivo → Abrir workspace desde archivo…`). Este workspace:
   - Configura GitHub Copilot Chat en español
   - Recomienda las extensiones necesarias (te aparece un popup para instalarlas)
   - Incluye tareas rápidas: abrir el curso, abrir la guía pre-clase, instalar dependencias Python
   - Carga automáticamente las skills, el agente y las instrucciones globales

> 💡 Si prefieres abrir la carpeta directamente sin workspace, usa `Archivo → Abrir carpeta…` y selecciona esta carpeta. Funciona igual, solo sin los atajos pre-configurados.

---

## 💰 ¿Cuánto cuesta?

| Herramienta | Costo | Notas |
|---|---|---|
| **VS Code** | Gratis | Editor de código de Microsoft |
| **Cuenta GitHub** | Gratis | Necesaria para todo lo demás |
| **GitHub Copilot Free** | Gratis | 2,000 completions + 50 chats al mes |
| **GitHub Copilot Pro** | ~$10 USD/mes | Acceso ilimitado a modelos premium (GPT-5, Claude Sonnet, Gemini) |
| **GitHub Copilot Pro+** | ~$39 USD/mes | Para usuarios power |
| Python (opcional) | Gratis | Para generar Excel/PowerPoint con scripts |

> ⚠️ Los precios pueden cambiar. Revisa la página oficial: <https://github.com/features/copilot/plans>

---

## 🧑‍💼 Casos de uso para gerentes de desarrollo y product managers

Este curso incluye **14 skills + 1 agente** diseñados para problemas reales de gestión. Las skills aplican a ambos roles — cada `SKILL.md` distingue el matiz por audiencia cuando es relevante.

| Caso de uso | Skill que ayuda |
|---|---|
| Planificar el próximo sprint | `plan-sprint` |
| Facilitar una retrospectiva | `retro-equipo` |
| Preparar 1:1s con tus reportes | `prep-one-on-one` |
| Generar reporte ejecutivo mensual | `generar-reporte-excel` + `generar-presentacion-pptx` |
| Analizar un Excel/PPT/PDF que te llegó | `analizar-archivos-existentes` |
| Reportar DORA metrics al liderazgo | `metricas-dora` |
| Hacer code review más rápido | `revisar-pr` |
| Onboarding de un nuevo ingeniero / PM | `onboarding-30-60-90` |
| Comunicar un outage productivo (status page + email + leadership) | `comunicado-incidente` |
| Status semanal a tu jefe / stakeholders | `reporte-status-semanal` |
| Postmortem real de un incidente (timeline, RCA, action items) | `postmortem-incidente` |
| Preparar una conversación difícil (feedback, despido, decir "no") | `conversacion-dificil` |
| Presentar a leadership (QBR, headcount, roadmap) | `prep-presentacion-leadership` |
| Conversaciones técnicas con contexto | Agente `Gerente de Desarrollo` |

### Skills globales adicionales (en inglés)

En `skills-globales/` se incluyen skills más generales reutilizables fuera del curso:

| Caso de uso | Skill |
|---|---|
| "Vamos a hacerle pre-mortem a esta decisión" (mi favorita para managers) | `postmortem` |
| Convertir hallazgos analíticos en reporte multi-audiencia | `analysis-report-authoring` |
| Análisis automatizado desde un modelo de Power BI vía MCP | `ba-automated-analysis` |
| Diccionario de columnas de un dataset (SQL/DAX) | `data-definitions-dictionary` |

Ver [`skills-globales/README.md`](skills-globales/README.md) para detalles y cómo activarlas a nivel global en tu máquina.

---

## 📖 Licencia

MIT — libre para uso personal y comercial.

---

**Hecho con ❤️ para acompañar a gerentes de desarrollo y product managers en su camino hacia la IA.**
