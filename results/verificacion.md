# Verificación computacional

Ejecución local propia. Tolerancia numérica: `1e-8`.

- SymPy verificó exactamente el sistema inicial y la identidad `(7a-2)/(10(1-a))`.
- También verificó la extensión: el ingreso laboral autónomo en `0<=a<=1/3` es `(14-15a)/(20(1-a))`, con derivada `-1/[20(1-a)^2]`.
- Se comprobaron 11 casos analíticos, incluido el punto de igualdad `a=2/7` y los extremos del tramo autónomo.
- En esos casos los rangos duales confirman salarios únicos, dentro de tolerancia.
- Un control con masas `(2/3,1/3)` y tipos `(0,1)` detecta correctamente multiplicidad: salarios bajos `[0,1/2]` y altos `[1,2]`.
- Barrido: 166 equilibrios, 83 capacidades y dos regímenes.
- Cada equilibrio pasó factibilidad primal/dual, complementariedad e igualdad de objetivos.
- Se conservan masas, `h=1/2` y `mu=10` en toda comparación entre regímenes.
- Las figuras muestran el modelo discreto propio. No son una reproducción exacta de las figuras continuas del paper.

## Comparación en a = 0.3

| Régimen | Salario L | Salario M | Salario H | Ingreso laboral | Cómputo | Producto |
|---|---:|---:|---:|---:|---:|---:|
| Sin IA | 0.200000 | 0.600000 | 1.600000 | 0.600000 | 0.000000 | 0.600000 |
| Copiloto | 0.300000 | 0.650000 | 1.400000 | 0.625000 | 0.000000 | 0.625000 |
| Autónoma | 0.214286 | 0.571429 | 2.000000 | 0.678571 | 3.000000 | 3.678571 |

## Reproducción

```bash
python -m pip install -r requirements.txt
python analysis/modelo_discreto.py
python analysis/verificar_y_graficar.py
```

Las versiones exactas están en `requirements.txt`. La optimización usa HiGHS a través de SciPy. No sustituye una demostración del equilibrio continuo ni una revisión semántica de Lean.
