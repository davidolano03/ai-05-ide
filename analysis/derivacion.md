# Derivación discreta y lectura económica

## 1. El recurso escaso es el tiempo de resolver excepciones

Una persona con conocimiento `z` resuelve por sí sola una fracción `z` de los problemas. Si trabaja, consulta por la fracción `1-z` restante. Cada consulta consume `h` unidades de tiempo del supervisor, sepa este o no la respuesta. Un supervisor puede atender

$$
 h(1-z)n(z)=1,\qquad n(z)=\frac1{h(1-z)}.
$$

Si su conocimiento es `s>z`, la empresa produce `n(z)s`, **no** `n(z)(z+s)`: el supervisor ya sabe resolver los problemas que resolvía el trabajador. Sumarlos contaría los mismos éxitos dos veces. Un trabajador más informado ahorra tiempo de consulta; un supervisor más informado mejora el resultado de todos sus trabajadores.

Con beneficio cero, por cada trabajador de tipo `i` asistido por `j`:

$$
 w_i+h(1-z_i)w_j=z_j.
$$

Para una organización que no se utiliza, el lado izquierdo debe ser al menos el derecho. Si fuera menor, una empresa entraría y ganaría dinero. Esta desigualdad permite revisar también las opciones descartadas.

## 2. Un ejemplo de tres tipos, resuelto sin caja negra

Fijamos masas divisibles, no tres personas indivisibles:

$$
(z_L,z_M,z_H)=(0,\tfrac12,1),\quad
(m_L,m_M,m_H)=(\tfrac12,\tfrac3{10},\tfrac15),\quad h=\tfrac12.
$$

Antes de IA, propongamos tres actividades. `x_ij` mide trabajadores, no empresas:

$$
x_{LM}=\tfrac15,\quad x_{LH}=\tfrac3{10},\quad x_{MH}=\tfrac15.
$$

Se utilizan exactamente los recursos:

$$
L:\ \tfrac15+\tfrac3{10}=\tfrac12,\qquad
M:\ \tfrac12\tfrac15+\tfrac15=\tfrac3{10},\qquad
H:\ \tfrac12\tfrac3{10}+\tfrac14\tfrac15=\tfrac15.
$$

Beneficio cero en las tres actividades da un sistema lineal:

$$
w_L+\tfrac12w_M=\tfrac12,\quad
w_L+\tfrac12w_H=1,\quad
w_M+\tfrac14w_H=1.
$$

Restar las dos primeras ecuaciones da `w_H-w_M=1`. Sustituirlo en la tercera produce

$$
(w_L,w_M,w_H)=(\tfrac15,\tfrac35,\tfrac85).
$$

Cada salario supera la productividad individual `(0,1/2,1)`. Por tanto, producir independientemente no ofrece beneficios positivos. El producto es

$$
Y=\tfrac15\tfrac12+\tfrac3{10}+\tfrac15=\tfrac35
=\tfrac12\tfrac15+\tfrac3{10}\tfrac35+\tfrac15\tfrac85.
$$

La última igualdad compara producción con pago total de recursos y certifica optimalidad junto con las desigualdades anteriores.

## 3. IA autónoma: umbral exacto en un tramo del ejemplo

Sea `a` la capacidad de IA, `mu=10` y `0<=a<=1/3`. La IA puede producir por sí sola, así que el cómputo sobrante fija `r=a`. Toda la masa baja trabaja con humanos medios: `x_LM=1/2`, usando `1/4` de supervisores medios. Quedan `1/20` de medios y `1/5` de altos para supervisar trabajadores de IA. Estos requieren

$$
x_{AM}=\frac{1}{10(1-a)},\quad x_{AH}=\frac{2}{5(1-a)}
$$

unidades de cómputo; el resto produce independientemente. Su suma es `1/[2(1-a)]<=3/4<10`, de modo que la abundancia se verifica, no se presupone sin revisar.

Los beneficios cero implican

$$
w_H^*=\frac{1-a}{\tfrac12(1-a)}=2,\quad
w_M^*=\frac{\tfrac12-a}{\tfrac12(1-a)}=\frac{1-2a}{1-a},\quad
w_L^*=\frac12-\frac12w_M^*=\frac{a}{2(1-a)}.
$$

El tramo es consistente: `w_M*>=1/2` exige `a<=1/3`; `w_L*>=a/2` descarta un beneficio positivo usando IA como supervisor de los bajos; `w_L*+w_H*/2>=1` y `w_M*+w_H*/4>=1` descartan las otras empresas humanas. Todos los salarios son al menos la productividad individual.

El cálculo decisivo, con denominador positivo, es

$$
w_L^*-\tfrac15=\frac{7a-2}{10(1-a)},\qquad
w_L^*>w_L\ \Longleftrightarrow\ a>\tfrac27.
$$

En `a=2/7` hay igualdad, no ganancia estricta. Para `a=1/10`, el salario bajo cae de `1/5` a `1/18`. Para `a=3/10`, sube a `3/14`. El salario alto pasa de `8/5` a `2` en ambos casos. La autonomía permanece fija: cambiar la capacidad cambia el signo del efecto abajo.

**Mecanismo:** los altos pasan a supervisar IA; los bajos quedan con supervisores medios. Cuando la IA es muy básica, los medios son escasos y caros como supervisores de IA, lo que reduce el salario bajo. Mejorar la IA reduce esa renta de los medios en este tramo y deja una fracción mayor del producto a los bajos. Un ganador abajo ni siquiera necesita adoptar IA directamente.

## 4. Copiloto: otro umbral, otra renta

Para `1/5<a<1/2`, una asignación factible usa `x_LH=1/4`, `x_MH=3/10` y `x_LA=1/4`. La IA consume solo `1/8` de cómputo; el resto está ocioso y `r^star=0`. De beneficio cero:

$$
w_L^\star=a,\quad w_H^\star=2(1-a),\quad w_M^\star=\frac{1+a}{2}.
$$

La empresa `LM` descartada no gana dinero porque `w_L^star+w_M^star/2=(1+5a)/4>=1/2` precisamente cuando `a>=1/5`. El supervisor alto prefiere trabajar en equipo a producir solo mientras `a<=1/2`. Así se justifican los límites del tramo. Para `a<1/5`, la asignación inicial sigue siendo óptima y la IA no se usa. En el punto `a=1/5` puede haber adopción indiferente en esta economía de átomos: el resultado exacto de no adopción de la proposición continua no se traslada automáticamente.

En `a=3/10`, los salarios son `(3/10,13/20,7/5)` y `Y^star=5/8`. Con autonomía son `(3/14,4/7,2)`, ingreso laboral `19/28`, renta total `3` y producción `103/28`. La gran diferencia de producto incluye el cómputo autónomo produciendo por sí solo. No es una mejora del salario promedio de esa misma magnitud.

## 5. Qué comprueba el programa

`modelo_discreto.py` construye una columna por actividad permitida. Maximiza `c'x` sujeto a `Ax<=b`, `x>=0`. Una columna humana `ij` produce `z_j`, consume un trabajador `i` y `h(1-z_i)` supervisores `j`. Las columnas IA agregan sus consumos de cómputo; el copiloto elimina producción independiente y trabajo de IA.

El dual minimiza `b'p` sujeto a `A'p>=c`, `p>=0`. Sus componentes humanos son salarios y el último es la renta del cómputo. El programa verifica factibilidad primal/dual, igualdad de objetivos y complementariedad con tolerancia `1e-8`. Además minimiza y maximiza cada salario sobre la cara dual óptima para detectar multiplicidad, en vez de confundir un vector del solver con unicidad.

Las restricciones permiten holgura. Como existe la actividad independiente de cada tipo, una holgura humana óptima solo puede ocurrir con productividad cero; se puede asignar a esa masa a producción independiente sin cambiar el producto. No se introduce una predicción de desempleo involuntario.

`verificar_y_graficar.py` contrasta las cuentas racionales con SymPy y con el solver. Produce tablas y gráficos a partir de los resultados, no de valores inventados.

## 6. Frontera de la traducción

Este ejemplo cambia el dominio del paper: tiene átomos, admite que distintas personas de un mismo tipo ocupen roles diferentes y no reproduce los intervalos de una distribución de densidad positiva. El umbral `2/7` no es el `bar a` universal del artículo. Las desigualdades del ejemplo sí muestran por qué omitir capacidad es incorrecto.

Como control adicional, el programa incluye dos tipos `(.2,.8)` con masas `(.8,.2)`. Allí el tipo más alto puede perder con IA autónoma de capacidad `.45` (salario `1.5` a `1.325`). Eso no refuta la Proposición 5: el ejemplo tiene átomos, el máximo conocimiento es `.8` y hay productores independientes antes de IA. Es una advertencia concreta contra exportar el teorema fuera de sus supuestos.

## 7. Dónde se corrigió una interpretación tentadora

La frase proporcionada por el profesor —«la distribución depende de autonomía, no capacidad»— omite dos umbrales. No se fabricó una conversación en la que otro LLM supuestamente hubiera defendido esa frase. La comprobación independiente consiste en leer las proposiciones con sus condiciones y resolver el ejemplo por álgebra, programación lineal y, donde la corrida lo logre, Lean. El estudiante debe hacer la cuenta a mano y escribir su propio veredicto antes de fotografiarla.

## 8. Extensión: mejor IA, más producto y menor ingreso laboral

Dentro del tramo autónomo del ejemplo, `0<=a<=1/3`, sumar los salarios ponderados por las masas da

$$
\mathcal L^*(a)=\frac12\frac{a}{2(1-a)}+\frac3{10}\frac{1-2a}{1-a}+\frac15\,2
=\frac{14-15a}{20(1-a)}.
$$

En el interior del tramo:

$$
\frac{d\mathcal L^*}{da}=-\frac1{20(1-a)^2}<0,\qquad
\frac{dY^*}{da}=\mu-\frac1{20(1-a)^2}>0\quad(\mu=10).
$$

La contribución marginal de los bajos es `1/[4(1-a)^2]`, la de los medios es `-3/[10(1-a)^2]` y la de los altos es cero. La caída de los medios pesa más. Simultáneamente, la renta total del cómputo aumenta a razón de `mu` por unidad de capacidad. Esta es una comparación **entre capacidades de IA autónoma**, distinta de comparar introducir IA con no tenerla. En todo este tramo, el ingreso laboral sigue superando el nivel pre-IA `3/5`.

SymPy verifica la identidad y su derivada. Es una extensión propia del modelo discreto, no una atribución de un teorema adicional al paper. No se extrapola a `a>1/3`, donde cambia la asignación de equilibrio.
