# Skills globales adicionales

Estas son **skills más generales** de mi librería personal, copiadas aquí para que tengan acceso fácil durante y después del curso. **No son específicas a gerencia de desarrollo**; son herramientas útiles para cualquier rol técnico/analítico.

## ⚠️ Diferencias con la carpeta `skills/`

| | `skills/` | `skills-globales/` |
|---|---|---|
| Idioma | Español | **Inglés** |
| Audiencia | Gerentes de desarrollo | General (analistas, PMs, devs, líderes) |
| Hecho para | Este curso | Reutilización amplia |
| Mantenimiento | Aquí en el repo del curso | Vienen de mi setup personal (`~/.copilot/skills/`) |

## Las 4 skills incluidas

### 🧠 `postmortem` — Análisis pre-mortem con honestidad brutal
La más recomendada para gerentes. Asume que tu plan/decisión **ya falló** y trabaja al revés para explicar por qué. Elimina sesgos de optimismo y "yes-man". Úsala cuando vayas a tomar una decisión grande: arquitectura, contratación, lanzamiento, presupuesto.

**Disparadores**: "postmortem", "pre-mortem", "qué podría salir mal", "reality check", "feedback brutal".

### 📝 `analysis-report-authoring` — Reportes analíticos multi-audiencia
Te ayuda a estructurar hallazgos (de cualquier análisis) en un reporte ejecutivo en markdown, con conversión a Word. Útil cuando tienes datos crudos y necesitas contarle la historia a leadership.

### 📊 `pptx-report-builder` — Decks ejecutivos con branding Microsoft
> ⚠️ **No incluida** porque se traslapa con `skills/generar-presentacion-pptx/` (que está en español y hecha para el curso). Si quieres la versión en inglés con assets de marca Microsoft, está en mi setup personal.

### 🤖 `ba-automated-analysis` — Análisis automatizado desde Power BI
Workflow end-to-end que conecta a un modelo de Power BI vía MCP, extrae datos con DAX, perfila columnas, corre análisis estadístico y genera reporte + dashboard HTML. **Requiere tener configurado un servidor MCP de Power BI** — sin eso no funciona.

### 📚 `data-definitions-dictionary` — Diccionario de columnas
Genera documentación de columnas de un dataset (SQL/DAX + CSV). Útil para onboarding a una nueva fuente de datos.

## Cómo activarlas

Cuando descargas este repo y lo abres en VS Code, Copilot las detecta automáticamente porque están bajo el workspace. Para forzar su uso explícitamente:

```
Usa la skill postmortem para hacer pre-mortem del plan de migración a microservicios que te voy a pegar abajo: ...
```

## Si las quieres a nivel global (todas tus conversaciones)

Cópialas a tu carpeta de skills de usuario:

```powershell
# Windows
$dest = "$env:USERPROFILE\.copilot\skills"
New-Item -ItemType Directory -Path $dest -Force | Out-Null
Copy-Item -Path .\skills-globales\* -Destination $dest -Recurse -Force
```

```bash
# macOS / Linux
mkdir -p ~/.copilot/skills
cp -r ./skills-globales/* ~/.copilot/skills/
```

Una vez ahí, Copilot las verá desde **cualquier** workspace que abras, no solo desde este repo.
