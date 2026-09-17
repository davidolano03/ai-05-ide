# Reproducir el contexto de AppliedModelingLib

`lean/` conserva la carpeta del paper sin modificarla. El scaffold también creó un módulo agregador fuera de esa carpeta y añadió el registro del módulo a `lakefile.toml`. Esos dos elementos se guardan aquí por separado.

En un clon de AppliedModelingLib fijado en `2db7d108cd3a2cb10148974bb2a77856e7d87428`:

1. Copiar `lean/` íntegro como `papers/IT25KnowledgeEconomy/`.
2. Copiar `IT25KnowledgeEconomy.lean` de esta carpeta como `papers/IT25KnowledgeEconomy.lean`.
3. Aplicar `lakefile.patch` desde la raíz del clon: `git apply RUTA/lakefile.patch`.
4. Instalar el toolchain indicado por `lean-toolchain` y las dependencias fijadas por el repositorio.
5. Ejecutar `lake env lean papers/IT25KnowledgeEconomy/MainTheorems.lean` para las cuatro pruebas algebraicas, y el check de contribución indicado en `LEAN_RUN.md` para conocer el estado del paper completo.

Un build del agregador puede admitir los `sorry` de `ProofInterface.lean`: compilar no convierte esas dos proposiciones en pruebas terminadas. El check de contribución tiene un alcance adicional de fuentes y auditoría. No se debe eliminar un fallo del check para presentar el resultado como completo.

Los archivos fuente privados y cachés no se publican. Para rehacer auditorías sobre el paper se requiere descargar la misma arXiv v11 y comprobar el SHA-256 documentado. En Windows, ver los ajustes locales registrados por la corrida; el entorno original no disponía de WSL.
