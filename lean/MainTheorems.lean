import Mathlib

/-!
# Checked finite consequences for *Artificial Intelligence in the Knowledge Economy*

The paper's equilibrium theorems are continuous. This file deliberately proves
only algebraic consequences of the displayed wage equations and a fully explicit
three-type extension. None of these results is presented as a proof of the
paper's continuous Propositions 1--6.
-/

namespace IT25KnowledgeEconomy

noncomputable section

/-! ## Proposition 2: displayed automated-top-firm wage identity -/

/-- The team size used in the paper: `n(z) = 1 / (h(1-z))`. -/
noncomputable def teamSize (h z : ℝ) : ℝ := (h * (1 - z))⁻¹

/--
The displayed zero-profit equation for a top-automated firm, together with
`r = a` and the paper's team-size identity, gives
`w = a(1 - h(1-z))`.

This is a conditional algebraic consequence of Proposition 2's displayed
equations, not a construction of the continuous equilibrium.
-/
theorem automatedWorkerWage_of_zeroProfit
    {n a w r h z : ℝ}
    (hn : n ≠ 0)
    (hzero : n * (a - w) - r = 0)
    (hrent : r = a)
    (hteam : 1 / n = h * (1 - z)) :
    w = a * (1 - h * (1 - z)) := by
  have hmul : n * (a - w) = a := by
    rw [hrent] at hzero
    linarith
  have hsub : a - w = a / n := by
    apply (eq_div_iff hn).2
    nlinarith [hmul]
  calc
    w = a - a / n := by linarith
    _ = a * (1 - 1 / n) := by ring
    _ = a * (1 - h * (1 - z)) := by rw [hteam]

/-! ## A transparent three-type extension -/

/-- Pre-AI wage of the bottom type in the checked three-type extension. -/
def baselineBottomWage : ℝ := 1 / 5

/-- Pre-AI wage of the middle type in the checked three-type extension. -/
def baselineMiddleWage : ℝ := 3 / 5

/-- Pre-AI wage of the top type in the checked three-type extension. -/
def baselineTopWage : ℝ := 8 / 5

/-- Bottom wage under autonomous AI in the checked three-type extension. -/
def autonomousBottomWage (a : ℝ) : ℝ := a / (2 * (1 - a))

/-- Middle wage under autonomous AI in the checked three-type extension. -/
def autonomousMiddleWage (a : ℝ) : ℝ := (1 - 2 * a) / (1 - a)

/-- Top wage under autonomous AI in the checked three-type extension. -/
def autonomousTopWage (_a : ℝ) : ℝ := 2

/-- Bottom wage under non-autonomous AI in the checked three-type extension. -/
def copilotBottomWage (a : ℝ) : ℝ := a

/-- Middle wage under non-autonomous AI in the checked three-type extension. -/
def copilotMiddleWage (a : ℝ) : ℝ := (1 + a) / 2

/-- Top wage under non-autonomous AI in the checked three-type extension. -/
def copilotTopWage (a : ℝ) : ℝ := 2 * (1 - a)

/--
For the three-type extension and `0 ≤ a ≤ 1/3`, the bottom type gains from
autonomous AI exactly when `a > 2/7`. This finite threshold result mirrors the
shape of Proposition 5 but is not its continuous theorem.
-/
theorem autonomousBottomWage_gt_baseline_iff
    {a : ℝ} (_ha0 : 0 ≤ a) (ha13 : a ≤ 1 / 3) :
    baselineBottomWage < autonomousBottomWage a ↔ (2 / 7 : ℝ) < a := by
  have hden : 0 < 2 * (1 - a) := by
    norm_num at ha13 ⊢
    nlinarith
  change (1 / 5 : ℝ) < a / (2 * (1 - a)) ↔ (2 / 7 : ℝ) < a
  constructor
  · intro h
    have hmul := (lt_div_iff₀ hden).1 h
    norm_num at hmul ⊢
    nlinarith
  · intro h
    apply (lt_div_iff₀ hden).2
    norm_num at h ⊢
    nlinarith

/--
In the common range `1/5 < a ≤ 1/3`, the bottom type earns strictly more under
non-autonomous AI than both in the baseline and under autonomous AI.
-/
theorem copilotBottomWage_dominates
    {a : ℝ} (ha15 : (1 / 5 : ℝ) < a) (ha13 : a ≤ 1 / 3) :
    baselineBottomWage < copilotBottomWage a ∧
      autonomousBottomWage a < copilotBottomWage a := by
  have ha0 : 0 < a := by
    norm_num at ha15 ⊢
    linarith
  have hden : 0 < 2 * (1 - a) := by
    norm_num at ha13 ⊢
    nlinarith
  constructor
  · exact ha15
  · change a / (2 * (1 - a)) < a
    apply (div_lt_iff₀ hden).2
    nlinarith

/--
In the same range, the top type earns strictly less with non-autonomous AI than
both in the pre-AI baseline and with autonomous AI. This is a finite analogue
of the top-income comparison in Proposition 6.
-/
theorem copilotTopWage_is_lower
    {a : ℝ} (ha15 : (1 / 5 : ℝ) < a) :
    copilotTopWage a < baselineTopWage ∧
      copilotTopWage a < autonomousTopWage a := by
  constructor <;>
    simp only [copilotTopWage, baselineTopWage, autonomousTopWage] <;>
    norm_num at ha15 ⊢ <;>
    linarith

end

end IT25KnowledgeEconomy
