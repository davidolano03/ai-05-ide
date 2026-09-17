# Cómo reproducir los materiales

## Economía y gráficos

Desde la raíz del repositorio, con Python 3.12:

```bash
python -m pip install -r requirements.txt
python analysis/modelo_discreto.py
python analysis/verificar_y_graficar.py
```

El primer comando de análisis escribe los casos de dos y tres tipos en `results/equilibrios.json`. El segundo verifica el álgebra con SymPy, contrasta los casos analíticos, calcula rangos de salarios en la cara dual óptima y ejecuta el barrido de capacidades. Genera las figuras y `results/verificacion.md`. Los gráficos del Beamer están en inglés.

Las masas son divisibles. `mu=10` se mantiene igual entre autonomía y copiloto. Los números son ilustrativos y no se calibraron a un país ni se estimaron con datos.

## Beamer

Se utilizó Tectonic 0.17.0. Con ese compilador disponible:

```bash
tectonic -k --keep-logs presentation.tex
```

También se pueden usar herramientas habituales de LaTeX con los paquetes estándar indicados en el preámbulo. La compilación requiere las figuras y `slides/lean-slide.tex`, incluidos en el repositorio. No tiene animaciones ni capturas del paper.

Para incorporar la evidencia personal, añadir `hand/derivacion.jpg` o `hand/derivacion.png` y recompilar. Antes de entregar, comprobar que la foto sea legible en pantalla y explicar la cuenta con palabras propias. Una foto poco legible no queda validada por compilar correctamente.

La revisión local del PDF utilizó PyMuPDF y Pillow con `analysis/revisar_presentacion.py`; esas dependencias de revisión son opcionales y no se necesitan para los cálculos económicos. El script renderiza páginas en `.work/slides-qa/`, comprueba límites del lienzo y permite inspección visual. Una comprobación automática de límites no sustituye mirar las diapositivas.

## Lean y procedencia

Seguir `LEAN_RUN.md`: allí deben constar la revisión de AppliedModelingLib, el compilador, los comandos realmente ejecutados y su salida. `lean/` es una copia de una carpeta de paper generada por la corrida; no se reorganiza para convertirla artificialmente en otro proyecto. No asumir que `lake build` en la raíz de este repositorio semanal ejecuta el check de AppliedModelingLib.

`prompts.md` contiene mensajes literales seleccionados de la sesión propia. `analysis/exportar_prompts.py` explica el filtro de exportación, pero la sesión privada original no se publica. Nunca se requiere subir archivos de autenticación o la caché local para reproducir la parte económica.
