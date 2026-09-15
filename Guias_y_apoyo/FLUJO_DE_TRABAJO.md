# Flujo de trabajo diario y actualizaciones

Esta guía es para cuando YA tienen el repositorio clonado y van a empezar a programar de forma regular. Sigue este flujo cada vez que te sientes a trabajar en el proyecto.

## 1. Antes de empezar a programar (siempre)

Nunca empieces a programar sin antes actualizar. Esto evita conflictos grandes después.

```bash
git checkout main
git pull
git checkout tu-rama
git merge main
```

Si aparecen conflictos aquí, resuélvelos antes de seguir (ver sección de conflictos más abajo).

## 2. Si vas a empezar algo nuevo, crea una rama con nombre descriptivo

No uses tu nombre solo — usa el nombre de lo que vas a hacer:

```bash
git checkout -b feature/nombre-de-la-funcionalidad
```

**Ejemplos buenos:**
- `feature/deteccion-color`
- `feature/interfaz-menu`
- `fix/error-division-cero`

**Evita:** `feature/hugo2`, `prueba`, `nueva-rama` — no dicen nada de qué trata.

## 3. Subir tus avances

```bash
git push
```

(La primera vez que subes una rama nueva, usa `git push -u origin nombre-de-tu-rama`.)

## 4. Cuando termines tu funcionalidad completa: abre un Pull Request

1. Ve a GitHub → pestaña **Pull requests** → **New pull request**.
2. Verifica `base: main` ← `compare: tu-rama`.
3. Describe brevemente qué hace tu código y si ya lo probaste.
4. Espera que otro compañero (no tú mismo) lo revise y apruebe.

## 5. Revisar el trabajo de otros

1. Entra a **Pull requests**, abre el PR de tu compañero.
2. Ve a **Files changed**, lee el código.
3. Si algo no está bien, comenta directo en la línea (ícono `+` azul al pasar el mouse).
4. Arriba a la derecha: **Review changes** → elige **Comment**, **Approve**, o **Request changes**.

## 6. Mergear a main

Una vez aprobado el PR:
1. Ve a la pestaña **Conversation**.
2. Clic en **Merge pull request** → **Confirm merge**.

## 7. Después de cada merge: todos actualizan

Avisen en el chat del equipo cuando algo se mergea, y cada quien corre:

```bash
git checkout main
git pull
git checkout tu-rama
git merge main
```

## 8. Marcar versiones importantes (tags)

Cuando lleguen a un punto importante (un avance funcional, una entrega al profesor), marquen esa versión. Esto lo hace normalmente quien coordina el repo, una vez que todo lo necesario ya está en `main`:

```bash
git checkout main
git pull
git tag -a v0.2-nombre-del-hito -m "Descripción breve de qué se logró"
git push origin v0.2-nombre-del-hito
```


Ver todos los tags:
```bash
git tag
```

En GitHub aparecen en la pestaña **Tags**, junto a Branches.

## 9. Si necesitas ver o recuperar una versión anterior

**Ver el historial de un archivo específico:**
```bash
git log --oneline -- nombre_archivo.py
```

**Ver cómo se veía un archivo en un commit específico:**
```bash
git show <hash-del-commit>:nombre_archivo.py
```

**Recuperar esa versión vieja a tu carpeta actual:**
```bash
git checkout <hash-del-commit> -- nombre_archivo.py
```

**Volver a ver el proyecto completo como estaba en un tag:**
```bash
git checkout v0.1-organizacion-completa
```
(Para volver a tu trabajo actual: `git checkout tu-rama`)

**Deshacer un cambio que ya se mergeó a main (sin borrar historial):**
```bash
git revert <hash-del-commit>
```

## 10. Si hay conflictos al hacer merge

Git te va a marcar en el archivo algo así:

```
<<<<<<< HEAD
tu código
=======
código de la otra persona
>>>>>>> main
```

1. Abre el archivo, decide qué parte(s) dejar (puedes combinar ambas si tiene sentido).
2. Borra las líneas `<<<<<<<`, `=======`, `>>>>>>>` una vez resuelto.
3. Guarda el archivo.
4. Ejecuta:
```bash
git add .
git commit -m "resuelve conflicto entre mi rama y main"
git push
```

**Para evitar conflictos grandes:** actualiza tu rama con `main` seguido (paso 1 de esta guía), y comunica al equipo antes de tocar un archivo que sabes que alguien más está usando.

## Resumen de comandos más usados

| Comando | Qué hace |
|---|---|
| `git checkout main && git pull` | Actualizar tu copia de main |
| `git checkout -b feature/nombre` | Crear rama nueva descriptiva |
| `git status` | Ver qué cambiaste |
| `git add .` | Preparar cambios |
| `git commit -m "prefijo: mensaje"` | Guardar avance |
| `git push` | Subir tu rama |
| `git merge main` | Traer cambios de main a tu rama |
| `git tag -a nombre -m "mensaje"` | Marcar una versión importante |
| `git log --oneline` | Ver historial de commits |
