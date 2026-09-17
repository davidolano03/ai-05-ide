# Guion de exposición, en español

El Beamer está en inglés por indicación del curso. Este guion ayuda a explicar el mecanismo; no conviene leerlo literalmente. Duración objetivo: **20 minutos**, con el apéndice fuera del recorrido principal. La sección Lean se debe ensayar con el estado definitivo de la corrida.

| Diapositiva | Tiempo | Punto que debe quedar claro |
|---|---:|---|
| 1. Portada | 0:20 | Paper 2025, Talamàs, versión v11 y enlace al repositorio |
| 2. Pregunta | 0:50 | Capacidad y autonomía son dos dimensiones |
| 3. Empresa | 1:25 | El tiempo para atender excepciones determina el equipo |
| 4. Condiciones | 1:00 | Los resultados no son incondicionales |
| 5. Proposición 5 | 1:30 | Ganadores abajo si y solo si se supera el umbral |
| 6. Proposición 6, adopción | 1:00 | El benchmark es el salario inicial, no cero |
| 7. Comparaciones | 1:05 | Cuantificadores, vecindades y desigualdades estrictas |
| 8. Mecanismo de precios | 1:10 | La autonomía cambia el costo de oportunidad del cómputo |
| 9. Tres tipos | 1:30 | Derivar y verificar el equilibrio inicial |
| 10. Umbral propio | 1:50 | La resta que determina el signo de la ganancia |
| 11. Salarios | 1:00 | Interpretar niveles y cambios sin confundirlos |
| 12. Producción | 0:50 | Separar renta del cómputo e ingreso laboral |
| 13. Computación | 0:50 | Qué certifican primal, dual y rangos de salarios |
| Lean | 3:00 | Matemática, código, prueba, interpretación y límites |
| Foto y veredicto | 1:50 | Comprobación personal auténtica y condición decisiva |
| Cierre | 0:50 | Contestar directamente la trampa del profesor |

## Explicaciones para acompañar las diapositivas

**2–3.** Imagino una oficina: quien sabe menos empieza casos rutinarios y remite las excepciones. El experto no crea un caso nuevo cuando responde: ayuda a terminar el que ya había empezado otra persona. Por eso no sumo las tasas de éxito `z+s`. Lo escaso es el tiempo del experto; incluso una consulta que no puede responder consume tiempo. Con `h=1/2`, un trabajador de conocimiento cero genera media unidad de carga esperada; el experto puede atender a dos trabajadores así. Un trabajador de conocimiento `1/2` solo genera un cuarto: el experto atiende a cuatro.

**4.** No basta decir «competencia perfecta». La densidad positiva, las dos capas, el cómputo abundante y `h<h0` hacen trabajo real. Este último supuesto asegura que organizarse es suficientemente atractivo como para que no haya productores independientes antes de IA. `a<1` también importa: el paper excluye la IA que sabe resolver todos los problemas. No afirmar que los de arriba ganan si se retira ese límite.

**5.** `B` no son todos los pobres, sino quienes están por debajo de la capacidad de IA y ganan respecto de su salario anterior. La proposición dice que ese conjunto es no vacío exactamente al superar cierto umbral. No dice que cualquier IA autónoma beneficie abajo. Tampoco dice que todos los tipos superiores a la IA ganen: los ganadores superiores forman una cola. El umbral cae dentro del conjunto inicial de trabajadores; incluso una IA que el paper llama «básica» puede ser suficientemente capaz para generar ganadores abajo.

**6–7.** ¿Por qué el copiloto debe superar `w(0)` si la persona de conocimiento cero no resuelve nada por sí misma? Porque ya podía producir dentro de una empresa con un supervisor humano. Su salario inicial refleja esa posibilidad. Por debajo del umbral no hay ganancias estrictas: el equilibrio coincide con el inicial. En las comparaciones de colas debo decir «existe una vecindad»; no ampliar el resultado a toda la distribución. En el extremo superior `z=1`, el enunciado solo asegura una comparación débil entre regímenes.

**8.** El cómputo abundante no es necesariamente gratuito. Si una unidad puede producir `a` por sí sola, dedicarla a asesorar tiene un costo de oportunidad `a`. Si solo puede asesorar y sobra, ese costo cae a cero. La diferencia entre `a-h(1-z)a` y `a` es el costo de ese asesoramiento. Pero estas expresiones solo valen para trabajadores que realmente usan IA. No puedo ponerlas sobre todos los salarios sin resolver primero la asignación.

**9–10.** Las tres ecuaciones igualan producto por trabajador y costo de recursos. Compruebo que la asignación usa exactamente las masas disponibles y que ninguna empresa descartada tiene beneficios positivos. Para el tramo autónomo, los bajos siguen con supervisores medios. Los altos y los medios restantes supervisan IA. La renta de los medios cambia, y por beneficio cero cambia lo que cobra el trabajador bajo. `a/(2(1-a))-1/5` se reduce a `(7a-2)/(10(1-a))`: el denominador es positivo en el tramo, por eso el signo depende solo de `7a-2`. En `2/7` hay indiferencia, no ganancia estricta.

**11.** En el panel izquierdo busco los cruces de cada curva con el salario inicial punteado, no comparo solo la pendiente. El quiebre de la curva autónoma indica un cambio de organización. Fuera de `a<=1/3`, la fórmula derivada en el slide anterior deja de describir todo el equilibrio: el programa vuelve a elegir las actividades. El programa no extrapola la fórmula de un tramo a otro.

**12.** La producción autónoma es grande en este ejemplo porque hay diez unidades de cómputo frente a una unidad de masa humana. El incremento no es diez veces la remuneración humana. Con competencia, producto es ingreso laboral más ingreso del cómputo. El programa muestra ambos sumandos.

**13.** El primal elige quién trabaja con quién. El dual pregunta qué precios hacen que ninguna empresa pueda ganar entrando. Si los recursos alcanzan, los precios descartan beneficios positivos y los dos objetivos coinciden, tengo una certificación numérica del óptimo del modelo finito. Los rangos duales evitan interpretar como unicidad lo que puede ser una selección arbitraria del solver. Tolerancia numérica no es prueba exacta de todos los valores del parámetro.

**Lean.** Usar la declaración real que aparece en el slide definitivo. Leer el dominio antes de la conclusión. Identificar dónde se demuestra la positividad del denominador y qué táctica transforma la desigualdad. Distinguir «esta prueba pasa Lean» de «las Proposiciones 5 y 6 quedaron demostradas desde los supuestos originales». Si quedan objetivos abiertos, nombrarlos y reportar el resultado real del check.

**Foto.** Esta parte requiere una hoja escrita por el estudiante. No presentar la derivación mecanografiada como evidencia manuscrita. Explicar qué paso se verificó personalmente, qué condición evita invertir la desigualdad al multiplicar y cuál es el veredicto propio. La frase sobre autonomía fue una hipótesis sugerida por el enunciado del profesor; no inventar que hubo una respuesta errónea específica de un LLM.

## Preguntas previsibles

- **¿El umbral es siempre `2/7`?** No. Es exacto para nuestras masas, tipos, `h` y el tramo especificado. El umbral continuo depende de la economía inicial.
- **¿Hay desempleo?** El modelo dispone de oportunidades abundantes; cambiar ocupaciones no equivale a perder empleo. Las predicciones de salario tampoco miden directamente vacantes.
- **¿Por qué el experto puede ganar más de una unidad?** Su conocimiento ayuda en varios problemas, aunque su tiempo disponible sea una unidad.
- **¿Un aumento de salario mide solo productividad?** No. Cambian tanto el emparejamiento como la división del producto según la escasez relativa.
- **¿Qué se pierde con tres tipos?** Densidad continua, intervalos de tipos y algunas propiedades de unicidad y asignación. Diferentes personas del tipo medio pueden ser trabajadores o supervisores.
- **¿Qué cambia por ser un artículo arbitrado?** La exposición separa resultados, supuestos y extensiones de forma disciplinada. El arbitraje no nos permite omitir condiciones ni atribuirle causalmente cada rasgo estilístico.
- **¿Lean prueba que la IA real hará esto?** No. Comprueba una deducción de un enunciado formal bajo sus supuestos. Validar el modelo empíricamente y verificar que la traducción representa el paper son tareas distintas.
