# Historial de comprobaciones y decisiones

Registro de hechos de esta ejecución. Los resultados vigentes están en `results/verificacion.md` y el resultado Lean en `LEAN_RUN.md`.

- La primera búsqueda encontró solo el README inicial y una rama `main` limpia. Se creó `codex/ide-talamas-entrega` antes de escribir los materiales.
- El Git del runtime no encontraba su auxiliar HTTPS. Se usó la instalación de Git de GitHub Desktop y se clonó AppliedModelingLib desde su repositorio oficial. No se reutilizó una formalización de otra persona.
- El primer intento de importar SciPy desde el sandbox no pudo leer los paquetes recién instalados. La ejecución con los permisos del usuario sí los pudo importar. Las dependencias permanecen locales en `.work/`.
- Una aserción inicial de SymPy comparaba la forma sintáctica de dos desigualdades. Se cambió por la comparación del conjunto solución exacto `(2/7,1)`. La corrección no cambia la desigualdad matemática.
- La exportación de gráficos como PDF falló porque Windows bloqueó una DLL de FontTools. Se exportaron gráficos PNG de alta resolución y se incorporaron al Beamer. El PDF de la presentación sí procede de compilar el `.tex` con Tectonic.
- Se revisaron los gráficos renderizados. Se corrigió una leyenda que coincidía con una etiqueta de producto y se separó la imagen del texto siguiente.
- El solver devolvió una solución dual única en los casos analíticos elegidos. Un control construido para tener varios precios produjo correctamente los intervalos `[0,1/2]` y `[1,2]`; por ello no se confundió selección del solver con unicidad general.
- El check de recursos, beneficios y complementariedad se aplicó también a las actividades que el equilibrio no utiliza. Verificar solo las ecuaciones activas no habría bastado para certificar un equilibrio.
- Se mantuvo explícita la diferencia entre las Proposiciones 5 y 6 del continuo y las identidades del ejemplo discreto. Un contraejemplo con otros tipos y productores independientes iniciales se interpreta como cambio de dominio.
- El PR se abrió en borrador con los pendientes visibles. No se fabricó una foto de manuscrito ni una respuesta previa de otro LLM para construir una historia de desconfianza.
