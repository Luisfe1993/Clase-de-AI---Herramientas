# 📋 Pre-Clase: Instalación de Herramientas

> **Tiempo estimado: 30–45 minutos.** Sigue estos pasos en orden algunos días antes de la clase. Si algo no funciona, no te preocupes — lo resolvemos en clase.

---

## ✅ Checklist rápido

- [ ] **Paso 1**: Crear cuenta de GitHub
- [ ] **Paso 2**: Instalar Git
- [ ] **Paso 3**: Instalar Visual Studio Code
- [ ] **Paso 4**: Iniciar sesión con tu cuenta de GitHub en VS Code
- [ ] **Paso 5**: Activar GitHub Copilot (plan Free o trial de Pro)
- [ ] **Paso 6**: Instalar la extensión "GitHub Copilot Chat" en VS Code
- [ ] **Paso 7** (opcional pero recomendado): Instalar Python 3.11+
- [ ] **Paso 8** (opcional): Instalar GitHub CLI (`gh`) para usar Copilot en terminal

---

## 1️⃣ Crear cuenta de GitHub (5 min)

1. Ve a <https://github.com/signup>
2. Usa un correo personal (no laboral si vas a hacer pruebas personales).
3. Elige un username — será tu identidad pública. Ejemplo: `mariarivera92`.
4. Verifica el correo desde tu bandeja de entrada.
5. ✅ Listo. Tienes una cuenta gratuita con repos públicos ilimitados.

> 💡 **No necesitas tarjeta de crédito** para esto.

---

## 2️⃣ Instalar Git (5 min)

Git es el sistema que usan los desarrolladores para versionar archivos.

### Windows
1. Descarga desde: <https://git-scm.com/download/win>
2. Ejecuta el instalador con los valores por defecto (siguiente → siguiente → instalar).
3. Abre **PowerShell** y verifica:
   ```powershell
   git --version
   ```
   Debe mostrar algo como `git version 2.50.x`.

### macOS
1. Abre **Terminal** y ejecuta:
   ```bash
   git --version
   ```
2. Si no está instalado, te ofrecerá instalar Xcode Command Line Tools. Acepta.

---

## 3️⃣ Instalar Visual Studio Code (5 min)

VS Code es el editor donde vamos a trabajar.

1. Descarga desde: <https://code.visualstudio.com/>
2. Elige tu sistema operativo (Windows / Mac / Linux).
3. Ejecuta el instalador.
   - **Windows**: marca las casillas *"Agregar al menú contextual"* y *"Agregar al PATH"*.
4. Ábrelo. Deberías ver la pantalla de bienvenida.

### Configura el idioma a español (opcional)

1. Presiona `Ctrl + Shift + X` (Windows) o `Cmd + Shift + X` (Mac) para abrir extensiones.
2. Busca: `Spanish Language Pack`
3. Instala y reinicia VS Code.

---

## 4️⃣ Iniciar sesión con GitHub en VS Code (3 min)

1. En VS Code, clic en el ícono de **Cuenta** (esquina inferior izquierda, un muñequito).
2. Clic en **Iniciar sesión con GitHub**.
3. Se abrirá tu navegador → autoriza el acceso.
4. Vuelve a VS Code. Verás tu username en la esquina.

---

## 5️⃣ Activar GitHub Copilot (5 min)

Tienes 3 opciones:

### Opción A — Copilot Free (recomendada para empezar)
- **Costo**: gratis
- **Incluye**: 2,000 autocompletados de código + 50 mensajes de chat al mes
- **Activación**: se activa automáticamente al iniciar sesión con tu cuenta de GitHub en VS Code.

### Opción B — Copilot Pro (recomendada para la clase)
- **Costo**: ~$10 USD/mes (gratis los primeros 30 días con tarjeta)
- **Incluye**: completions ilimitados, chat ilimitado, acceso a GPT-5, Claude Sonnet 4.5, Gemini Pro
- **Activación**: <https://github.com/settings/copilot>

### Opción C — Copilot Pro+
- **Costo**: ~$39 USD/mes
- Solo si vas a usarlo muy intensivamente.

> 💡 Para esta clase **Copilot Free es suficiente**. Si quieres aprovechar al máximo los modelos premium, considera el trial de Pro de 30 días.

📎 Página oficial de planes: <https://github.com/features/copilot/plans>

---

## 6️⃣ Instalar la extensión GitHub Copilot Chat (3 min)

> ℹ️ En VS Code reciente, **GitHub Copilot Chat ya viene preinstalado**. Solo verifica.

1. En VS Code, presiona `Ctrl + Shift + X` (o `Cmd + Shift + X`).
2. Busca: `GitHub Copilot Chat`
3. Si dice **Instalar**, instálala. Si dice **Desinstalar**, ya la tienes.
4. Verifica que también esté instalada **GitHub Copilot** (sin "Chat" — es la del autocompletado).

### Verificar que funciona

1. Presiona `Ctrl + Alt + I` (Windows) o `Cmd + Ctrl + I` (Mac) para abrir el chat.
2. Escribe: `Hola, ¿funcionas?`
3. Si te responde, **¡todo está listo!** 🎉

---

## 7️⃣ Instalar Python 3.11+ (opcional pero recomendado)

Lo usaremos para generar **Excel** y **PowerPoint** con código generado por la AI.

### Windows
1. Descarga desde: <https://www.python.org/downloads/>
2. **IMPORTANTE**: durante la instalación marca la casilla ✅ **"Add python.exe to PATH"**.
3. Abre PowerShell y verifica:
   ```powershell
   python --version
   pip --version
   ```

### macOS
1. Instala con [Homebrew](https://brew.sh/):
   ```bash
   brew install python@3.12
   ```
2. Verifica:
   ```bash
   python3 --version
   ```

### Librerías que usaremos en clase

No las instales aún — lo haremos juntos. Pero estas son las que veremos:
- `openpyxl` — generar archivos Excel
- `python-pptx` — generar PowerPoint
- `pandas` — manipular datos

---

## 8️⃣ GitHub CLI (`gh`) — opcional

GitHub CLI te permite usar Copilot desde la terminal con comandos como `gh copilot suggest` y `gh copilot explain`.

### Windows
```powershell
winget install --id GitHub.cli
```

### macOS
```bash
brew install gh
```

### Autenticarte
```bash
gh auth login
```
- Selecciona: `GitHub.com` → `HTTPS` → `Login with a web browser`
- Copia el código que aparece y pégalo en el navegador.

### Instalar Copilot CLI extension
```bash
gh extension install github/gh-copilot
gh copilot --version
```

> ⚠️ `gh copilot` requiere una suscripción activa a Copilot (Free, Pro o Pro+).

---

## 🆘 Si algo no funciona

No te estreses. Llega a clase con lo que hayas logrado instalar y anota qué paso falló. Lo resolvemos juntos.

### Errores comunes

| Error | Solución |
|---|---|
| `git no se reconoce como comando` | Reinicia PowerShell/Terminal después de instalar Git. Si persiste, reinstala marcando "Add to PATH". |
| Copilot Chat no responde | Cierra sesión en VS Code (ícono cuenta → Cerrar sesión) y vuelve a entrar. |
| "You don't have access to Copilot" | Activa el plan Free en <https://github.com/settings/copilot>. |
| `python` no funciona pero `python3` sí (Mac) | Usa siempre `python3` en Mac, es normal. |

---

## 📝 ¿Qué traer a clase?

- ✅ Tu laptop con todo lo de arriba instalado.
- ✅ Tu cuenta de GitHub funcionando.
- ✅ Cargador de la laptop.
- ✅ Una taza de café ☕ (opcional pero recomendado).

---

**Nos vemos en clase 👋**
