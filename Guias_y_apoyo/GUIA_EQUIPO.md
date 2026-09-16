# Guía rápida para empezar a colaborar

## Paso 0: Requisitos previos
- Tener **Git** instalado (descarga en git-scm.com si no lo tienen).
- Tener **Python** y **Spyder** instalados (Anaconda los incluye a ambos).
- Tener cuenta de **GitHub** y haber aceptado la invitación como colaborador que Hugo les envió.


## Paso 1: Clona el repositorio

Abre Git Bash, ubícate en una carpeta VACÍA donde quieras guardar el proyecto y ejecuta:

 
```bash
git clone https://github.com/blackcyber-cyber/PROGRAMACION_AVANZADA.git
cd PROGRAMACION_AVANZADA
```
 
## Paso 2: Crea tu propia rama
 
**Nunca trabajes directo sobre `main`.** Crea tu rama personal:
 
```bash
git checkout -b feature/nombre_o_funcion
#Recordar que solo se hace una rama ppor trabajo, es decir que si te toca el tema "Catalogo" y "tickest" deberas crear dos rmas una para cada una
```
 
Ejemplo real: `git checkout -b feature/carrito_de_compras`
 
## Estructura del repositorio
 
```
PROGRAMACION_AVANZADA/
├── codigo_principal/          ← archivos principales del programa (ej. main.py)
├── funciones_complementarios/ ← funciones de apoyo reutilizables
├── Guias_y_apoyo/              ← material de referencia, apuntes, guías
├── README.md
├── CONTRIBUTING.md
├── GUIA_EQUIPO.md
└── .gitignore
```
 
**Guarda tu código en la carpeta que corresponda según su función. No dejes archivos `.py` sueltos en la raíz del proyecto.**
 
## Paso 3: Abre la carpeta en Spyder
 
- En Spyder: **Archivo > Abrir**, navega a la carpeta `PROGRAMACION_AVANZADA` que acabas de clonar.
- Crea o edita tus archivos `.py` **dentro de la subcarpeta que corresponda** (`codigo_principal/` o `funciones_complementarios/`), no sueltos en la raíz.
- Guarda con `Ctrl+S`.
## Paso 5: Sube tus cambios (cada vez que avances algo)
 
```bash
git status
```
Revisa qué archivos cambiaste (aparecen en rojo).
 
```bash
git add .
```
Agrega todos los cambios. (O `git add nombre_archivo.py` para uno específico.)
 
```bash
git commit -m "descripcion clara de lo que hiciste"
```
Guarda el avance con un mensaje.
 
> Recuerda: si creas un archivo nuevo, asegúrate de que quede dentro de `codigo_principal/`, `funciones_complementarios/` o `Guias_y_apoyo/`, según corresponda.
 
```bash
git push -u origin feature/tu-nombre
```
Sube tu rama a GitHub (solo la **primera vez**; después basta con `git push`).
 
## Paso 4: Abre un Pull Request en GitHub
 
1. Entra a https://github.com/blackcyber-cyber/PROGRAMACION_AVANZADA
2. Verás un aviso para crear un PR desde tu rama recién subida — dale clic a **"Compare & pull request"**.
3. Verifica que diga `base: main` ← `compare: feature/tu-nombre`.
4. Pon un título y describe brevemente qué hiciste.
5. Dale clic a **"Create pull request"**.
## Paso 5: Espera revisión (o revisa el de otro)
 
- Alguien más del equipo (no tú mismo) debe revisar tu PR en la pestaña **"Files changed"** y aprobarlo.
- Si te toca revisar el de alguien más, entra al PR, revisa el código, y si está bien, aprueba.
## Paso 6: Mergear a main
 
Una vez aprobado, en la pestaña **"Conversation"** del PR:
1. Clic en **"Merge pull request"**.
2. Clic en **"Confirm merge"**.
## Paso 7: Actualiza tu copia local después del merge
 
```bash
git checkout main
git pull
```
 
## Paso 8: Para seguir trabajando después
 
Cada vez que empieces a programar de nuevo:
 
```bash
git checkout main
git pull
git checkout feature/tu-nombre
git merge main
```
 
Esto trae los cambios más recientes del equipo a tu rama antes de seguir, para evitar conflictos grandes al final.
 
## Resumen de comandos más usados
 
| Comando | Qué hace |
|---|---|
| `git status` | Ver qué archivos cambiaste |
| `git add .` | Preparar todos los cambios para commit |
| `git commit -m "mensaje"` | Guardar los cambios preparados |
| `git push` | Subir tus commits a GitHub |
| `git pull` | Traer los cambios más recientes de GitHub |
| `git checkout -b nombre-rama` | Crear y cambiarte a una rama nueva |
| `git checkout nombre-rama` | Cambiarte a una rama existente |
| `git branch` | Ver en qué rama estás y cuáles existen |
| `git merge main` | Traer los cambios de main a tu rama actual |
 
## Importante: no editar directo en main
 
`main` está protegida — no van a poder hacer `git push` directo ahí. Siempre trabajen en su rama y suban por Pull Request.
 
## Sobre versiones (tags)
 
Cuando el equipo llegue a un avance importante (por ejemplo, para entregar al profesor), alguien puede marcar esa versión:
 
```bash
git checkout main
git pull
git tag -a v1.0 -m "Primer avance funcional"
git push origin v1.0
```
 
Esto no lo hace cada persona — normalmente lo hace quien coordina el repo (Hugo), una vez que todo el trabajo de esa entrega ya está en `main`.
