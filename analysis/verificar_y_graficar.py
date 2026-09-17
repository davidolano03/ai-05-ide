"""Comprueba las derivaciones y genera las figuras en inglés para el Beamer."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from modelo_discreto import solve

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
FIG = ROOT / "figures"
OUT.mkdir(exist_ok=True)
FIG.mkdir(exist_ok=True)
a = sp.symbols("a", real=True)
wl = a / (2 * (1-a))
assert sp.simplify(wl-sp.Rational(1,5)-(7*a-2)/(10*(1-a))) == 0
assert sp.solve_univariate_inequality(wl > sp.Rational(1,5), a, relational=False) == sp.Interval.open(sp.Rational(2,7),1)
L, M, H = sp.symbols("L M H")
solution = sp.solve([L+M/2-sp.Rational(1,2), L+H/2-1, M+H/4-1], [L,M,H])
assert solution == {L:sp.Rational(1,5), M:sp.Rational(3,5), H:sp.Rational(8,5)}

z, masses, h, mu = [0,.5,1], [.5,.3,.2], .5, 10
baseline = solve(z, masses, h)
checks = [baseline]
for capacity in [0,.1, .2, 2/7,.3,1/3]:
    r = solve(z, masses, h, capacity, mu, "autonomous")
    expected = [capacity/(2*(1-capacity)), (1-2*capacity)/(1-capacity), 2]
    assert np.allclose(r["wages"], expected, atol=1e-8)
    assert abs(r["rent"]-capacity) < 1e-8
    checks.append(r)
for capacity in [.21,.3,.45,.49]:
    r = solve(z, masses, h, capacity, mu, "copilot")
    assert np.allclose(r["wages"], [capacity,(1+capacity)/2,2*(1-capacity)], atol=1e-8)
    assert abs(r["rent"]) < 1e-8
    checks.append(r)
for r in checks:
    assert max(hi-lo for lo,hi in r["wage_ranges"]) < 1e-7
    assert abs(r["output"]-r["labor_income"]-r["capital_income"]) < 1e-8

# A balanced two-type economy has an interval of supporting wages.
degenerate = solve([0,1], [2/3,1/3], .5)
assert degenerate["wage_ranges"][0][1]-degenerate["wage_ranges"][0][0] > .1
assert np.allclose(degenerate["wage_ranges"], [[0,.5],[1,2]], atol=1e-8)
(OUT/"control_multiplicidad.json").write_text(json.dumps(degenerate, indent=2),encoding="utf-8")

grid = np.unique(np.r_[np.linspace(0,.8,81), .2, 2/7, 1/3, .5])
sweep = []
for capacity in grid:
    for regime in ["autonomous", "copilot"]:
        sweep.append(solve(z,masses,h,float(capacity),mu,regime))
(OUT/"barrido.json").write_text(json.dumps(sweep,indent=2),encoding="utf-8")
plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":11,
                    "axes.spines.top":False,"axes.spines.right":False})
colors = {"autonomous":"#126d87", "copilot":"#c96a24"}
fig, ax = plt.subplots(1,3,figsize=(12.5,3.4),sharex=True)
for i,title in enumerate(["Low knowledge: z = 0", "Middle: z = 1/2", "High: z = 1"]):
    ax[i].axhline(baseline["wages"][i], color="#666666",linestyle=":",label="Before AI")
    for regime,label in [("autonomous","Autonomous"),("copilot","Co-pilot")]:
        rows=[r for r in sweep if r["regime"]==regime]
        ax[i].plot(grid,[r["wages"][i] for r in rows],label=label,color=colors[regime],lw=2.2)
    ax[i].set_title(title, fontsize=12)
    ax[i].set_xlabel("AI capability a")
    ax[i].grid(alpha=.15)
ax[0].set_ylabel("Wage per unit of human time")
ax[0].axvline(2/7,color=colors["autonomous"],alpha=.4,linestyle="--")
ax[0].axvline(.2,color=colors["copilot"],alpha=.4,linestyle="--")
ax[0].legend(frameon=False,fontsize=9,loc="upper left")
fig.tight_layout()
fig.savefig(FIG/"wages.png",dpi=240,bbox_inches="tight")
plt.close(fig)

selected=[baseline,solve(z,masses,h,.3,mu,"copilot"),solve(z,masses,h,.3,mu,"autonomous")]
fig,ax=plt.subplots(figsize=(8.4,3.1))
y=np.arange(3)
labor=np.array([r["labor_income"] for r in selected])
capital=np.array([r["capital_income"] for r in selected])
ax.barh(y,labor,color="#126d87",label="Labor income")
ax.barh(y,capital,left=labor,color="#a6c9ce",label="Compute income")
for i,r in enumerate(selected):
    ax.text(r["output"]+.04,i,f'{r["output"]:.3f}',va="center",fontsize=11)
ax.set_yticks(y,["Before AI","Co-pilot, a = 0.3","Autonomous, a = 0.3"])
ax.invert_yaxis()
ax.set_xlim(0,4.15)
ax.set_xlabel("Total output = labor income + compute income")
ax.legend(frameon=False,loc="upper right",fontsize=10)
fig.tight_layout()
fig.savefig(FIG/"output.png",dpi=240,bbox_inches="tight")
plt.close(fig)

lines=["# Verificación computacional", "", "Ejecución local propia. Tolerancia numérica: `1e-8`.","",
       "- SymPy verificó exactamente el sistema inicial y la identidad `(7a-2)/(10(1-a))`.",
       "- Se comprobaron 11 casos analíticos, incluido el punto de igualdad `a=2/7` y los extremos del tramo autónomo.",
       "- En esos casos los rangos duales confirman salarios únicos, dentro de tolerancia.",
       "- Un control con masas `(2/3,1/3)` y tipos `(0,1)` detecta correctamente multiplicidad: salarios bajos `[0,1/2]` y altos `[1,2]`.",
       f"- Barrido: {len(sweep)} equilibrios, {len(grid)} capacidades y dos regímenes.",
       "- Cada equilibrio pasó factibilidad primal/dual, complementariedad e igualdad de objetivos.",
       "- Se conservan masas, `h=1/2` y `mu=10` en toda comparación entre regímenes.",
       "- Las figuras muestran el modelo discreto propio. No son una reproducción exacta de las figuras continuas del paper.","",
       "## Comparación en a = 0.3", "", "| Régimen | Salario L | Salario M | Salario H | Ingreso laboral | Cómputo | Producto |",
       "|---|---:|---:|---:|---:|---:|---:|"]
for label,r in zip(["Sin IA","Copiloto","Autónoma"],selected):
    nums=r["wages"]+[r["labor_income"],r["capital_income"],r["output"]]
    lines.append("| "+label+" | "+" | ".join(f"{v:.6f}" for v in nums)+" |")
lines += ["", "## Reproducción", "", "```bash", "python -m pip install -r requirements.txt",
          "python analysis/modelo_discreto.py", "python analysis/verificar_y_graficar.py", "```", "",
          "Las versiones exactas están en `requirements.txt`. La optimización usa HiGHS a través de SciPy. No sustituye una demostración del equilibrio continuo ni una revisión semántica de Lean."]
(OUT/"verificacion.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
print("PASS: álgebra simbólica, equilibrios analíticos, control de multiplicidad y",len(sweep),"equilibrios del barrido.")
