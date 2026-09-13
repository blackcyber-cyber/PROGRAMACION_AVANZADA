# Guía de contribución

Reglas de trabajo en equipo para este repositorio. Somos 4 personas, así que seguimos este flujo para evitar pisarnos el código entre nosotros.

## 1. Antes de empezar (una sola vez por persona)

```bash
git clone https://github.com/blackcyber-cyber/PROGRAMACION_AVANZADA.git
cd PROGRAMACION_AVANZADA
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@ejemplo.com"
```

## 2. Reglas básicas

- **Nunca se trabaja directo sobre `main`.** Todo cambio pasa por una rama y un Pull Request (PR).
- Antes de crear una rama nueva, actualiza tu `main` local:
  ```bash
  git checkout main
  git pull
  ```
- Crea tu rama con un nombre claro (por persona o por módulo):
  ```bash
  git checkout -b feature/tu-nombre
  # o por función: feature/interfaz, feature/logica-juego, etc.
  ```

## 3. Guardar y subir tus cambios

```bash
git add .
git commit -m "Mensaje claro de qué hiciste"
git push -u origin feature/tu-nombre
```

Después de la primera vez, basta con `git push`.

### Convención de mensajes de commit

| Prefijo    | Cuándo usarlo                          |
|------------|-----------------------------------------|
| `feat:`    | Agregas una funcionalidad nueva         |
| `fix:`     | Corriges un error                       |
| `docs:`    | Cambios solo en documentación           |
| `refactor:`| Reordenas código sin cambiar su función |

Ejemplo: `git commit -m "feat: agrega validación de usuario"`

## 4. Abrir un Pull Request

1. Ve al repositorio en GitHub, verás el botón **"Compare & pull request"**.
2. Escribe un título y describe brevemente qué cambia y por qué.
3. Asegúrate de que la rama destino sea `main`.
4. Espera revisión antes de mergear.

## 5. Revisión de código

- Al menos otra persona del equipo debe revisar el PR antes de aprobarlo.
- Evita aprobar tu propio PR.
- Si hay observaciones, corrígelas en la misma rama y vuelve a hacer `git push`; el PR se actualiza solo.

## 6. Actualizar tu rama con los cambios del equipo

Si mientras trabajas otros ya mergearon cosas a `main`, actualiza tu rama para evitar conflictos grandes al final:

```bash
git checkout main
git pull
git checkout feature/tu-nombre
git merge main
```

Si hay conflictos, Git te los marcará en los archivos afectados. Resuélvelos manualmente, luego:

```bash
git add .
git commit -m "Resuelve conflictos con main"
git push
```

## 7. Después del merge

Una vez que tu PR fue aprobado y mergeado a `main`, todos deben traer los cambios:

```bash
git checkout main
git pull
```

## 8. Sobre el `.gitignore`

Este repo usa la plantilla de Python. Ignora archivos temporales o generados automáticamente (`__pycache__/`, entornos virtuales, `.env`, etc.), **nunca tu código fuente**. No necesitas tocarlo salvo que agreguen alguna herramienta nueva que genere otro tipo de archivos temporales.

## 9. Comunicación

- Antes de tocar un archivo que sabes que alguien más está usando, avisa en el chat del equipo.
- Si dos personas van a trabajar en el mismo módulo, divídanse por funciones dentro del archivo para minimizar conflictos.
