"""Economía de dos capas como programa lineal. Ejecutar desde cualquier carpeta.

Las masas son divisibles. Cada columna mide trabajadores (no empresas).
Los salarios son precios duales de una unidad de tiempo humano.
No identifica este modelo finito con los teoremas del continuo.
"""
from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parents[1]


def solve(z, masses, h, a=None, mu=0.0, regime="none"):
    z, masses = np.asarray(z, float), np.asarray(masses, float)
    assert len(z) == len(masses) and np.all(np.diff(z) > 0)
    assert np.all((0 <= z) & (z <= 1)) and np.all(masses > 0)
    assert 0 < h < 1 and regime in {"none", "autonomous", "copilot"}
    use_ai = regime != "none"
    if use_ai:
        assert a is not None and 0 <= a < 1 and mu > 0
    n = len(z)
    cols, outputs, labels = [], [], []

    def add(label, output, resources):
        col = np.zeros(n + int(use_ai))
        for idx, value in resources.items():
            col[idx] = value
        cols.append(col)
        outputs.append(output)
        labels.append(label)

    for i in range(n):
        add(f"independent_{i}", z[i], {i: 1})
        for j in range(i + 1, n):
            add(f"human_{i}_{j}", z[j], {i: 1, j: h * (1 - z[i])})
    if use_ai:
        for i in range(n):
            if z[i] < a:
                add(f"ai_solver_{i}", a, {i: 1, n: h * (1 - z[i])})
            if regime == "autonomous" and a < z[i]:
                add(f"ai_worker_{i}", z[i], {i: h * (1 - a), n: 1})
        if regime == "autonomous":
            add("ai_independent", a, {n: 1})
    A = np.array(cols).T
    c = np.array(outputs)
    b = np.r_[masses, mu] if use_ai else masses
    result = linprog(-c, A_ub=A, b_ub=b, bounds=(0, None), method="highs")
    if not result.success:
        raise RuntimeError(result.message)
    prices = -result.ineqlin.marginals
    primal = float(c @ result.x)
    dual = float(b @ prices)
    slack = b - A @ result.x
    reduced = A.T @ prices - c
    tol = 1e-8
    assert min(slack) > -tol and min(reduced) > -tol
    assert abs(primal - dual) < tol
    assert max(abs(result.x * reduced)) < tol
    assert max(abs(slack * prices)) < tol
    # A dual optimum need not be unique in an atomic economy. Bound each wage
    # on the exact optimal dual face instead of assuming solver uniqueness.
    ranges = []
    for i in range(n):
        direction = np.eye(len(b))[i]
        lo = linprog(direction, A_ub=-A.T, b_ub=-c, A_eq=[b], b_eq=[primal],
                     bounds=(0, None), method="highs")
        hi = linprog(-direction, A_ub=-A.T, b_ub=-c, A_eq=[b], b_eq=[primal],
                     bounds=(0, None), method="highs")
        assert lo.success and hi.success
        ranges.append([float(lo.fun), float(-hi.fun)])
    return {"regime": regime, "a": a, "h": h, "mu": mu, "z": z.tolist(),
            "masses": masses.tolist(), "wages": prices[:n].tolist(),
            "wage_ranges": ranges, "rent": float(prices[-1]) if use_ai else 0,
            "output": primal, "labor_income": float(masses @ prices[:n]),
            "capital_income": float(mu * prices[-1]) if use_ai else 0,
            "primal_dual_gap": abs(primal - dual),
            "unused_resources": slack.tolist(),
            "activities": {k: float(v) for k, v in zip(labels, result.x) if v > tol}}


def main():
    cases = []
    for z, masses in [([.2, .8], [.8, .2]), ([0, .5, 1], [.5, .3, .2])]:
        cases.append(solve(z, masses, .5))
        for a in [.1, .3, .45, .7]:
            for regime in ["autonomous", "copilot"]:
                cases.append(solve(z, masses, .5, a, 10, regime))
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    (out / "equilibrios.json").write_text(json.dumps(cases, indent=2), encoding="utf-8")
    for r in cases:
        print(len(r["z"]), r["a"], r["regime"],
              "w=", np.round(r["wages"], 6), "Y=", round(r["output"], 6))


if __name__ == "__main__":
    main()
