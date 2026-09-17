import IT25KnowledgeEconomy.MainTheorems
import IT25KnowledgeEconomy.Assumptions

/-!
# Source-facing interface: *Artificial Intelligence in the Knowledge Economy*

The complete normal-scope inventory is the competitive-equilibrium definition
and Propositions 1--6.  This partial interface expands Propositions 5 and 6,
the two priority results, without claiming their continuous equilibrium proofs.
Propositions 1--4 remain inventoried but do not yet have source-matching Specs.

`sourceModelAssumptions` below is deliberately visible.  It records the open
bridge from the paper's continuous economy (density, measurable allocation,
matching resource equation, zero-profit firm optimization, and market clearing)
to these result-shaped carriers.  It is not a proof of that bridge and prevents
the declarations below from being reported as completed paper theorems.
-/

namespace IT25KnowledgeEconomy

noncomputable section

abbrev WageSchedule := ℝ → ℝ

/-- The paper's order `A ≼ B`: every knowledge type in `A` is below every type in `B`. -/
def LiesBelow (A B : Set ℝ) : Prop :=
  ∀ ⦃a⦄, a ∈ A → ∀ ⦃b⦄, b ∈ B → a ≤ b

/-- Humans weakly below the AI knowledge level whose autonomous-AI wage rises. -/
def bottomWinners
    (preWage autonomousWage : WageSchedule) (aiKnowledge : ℝ) : Set ℝ :=
  {z | z ∈ Set.Icc (0 : ℝ) aiKnowledge ∧ preWage z < autonomousWage z}

/-- Humans weakly above the AI knowledge level whose autonomous-AI wage rises. -/
def topWinners
    (preWage autonomousWage : WageSchedule) (aiKnowledge : ℝ) : Set ℝ :=
  {z | z ∈ Set.Icc aiKnowledge (1 : ℝ) ∧ preWage z < autonomousWage z}

/--
Result-shaped data needed to state Proposition 5.  The first field is an
explicit open boundary: the current Lean development has not constructed the
paper's continuous equilibria from its primitive model.
-/
structure PropositionFiveModel where
  sourceModelAssumptions : Prop
  preAIWorkers : Set ℝ
  preAIWage : WageSchedule
  autonomousAIWage : ℝ → WageSchedule

/--
Proposition 5 (pp. 23--24): bottom winners exist exactly above a threshold in
the interior of the pre-AI worker set, while top winners exist for every
non-superintelligent AI knowledge level.

The conclusion is represented clause-for-clause.  The visible
`sourceModelAssumptions` field does not yet encode the paper's continuous model,
so this draft Spec is neither a derivable model bridge nor a completed
source-faithful formalization.
-/
def propositionFiveSpec : Prop :=
  ∀ d : PropositionFiveModel,
    d.sourceModelAssumptions →
      ∃ cutoff : ℝ,
        cutoff ∈ interior d.preAIWorkers ∧
          ∀ aiKnowledge : ℝ,
            aiKnowledge ∈ Set.Ico (0 : ℝ) 1 →
              ((bottomWinners d.preAIWage (d.autonomousAIWage aiKnowledge)
                    aiKnowledge).Nonempty ↔ cutoff < aiKnowledge) ∧
                (topWinners d.preAIWage (d.autonomousAIWage aiKnowledge)
                    aiKnowledge).Nonempty

/-- Equilibrium observables used by the result-shaped Proposition 6 interface. -/
structure EquilibriumOutcome where
  wage : WageSchedule
  computeRent : ℝ
  output : ℝ
  laborIncome : ℝ
  aiAssistedWorkers : Set ℝ
  peopleAssistedWorkers : Set ℝ
  independentProducers : Set ℝ
  peopleSolvers : Set ℝ

/--
Result-shaped data needed to state Proposition 6.  Feasibility and equilibrium
are explicit predicates because their construction from the paper's continuous
primitives remains the main unformalized obligation.
-/
structure PropositionSixModel where
  sourceModelAssumptions : Prop
  aiKnowledge : ℝ
  preAI : EquilibriumOutcome
  autonomousAI : EquilibriumOutcome
  feasibleNonAutonomous : EquilibriumOutcome → Prop
  nonAutonomousEquilibrium : EquilibriumOutcome → Prop

/-- Output efficiency among allocations feasible under the non-autonomous regime. -/
def EfficientNonAutonomous
    (d : PropositionSixModel) (e : EquilibriumOutcome) : Prop :=
  ∀ f, d.feasibleNonAutonomous f → f.output ≤ e.output

/-- Labor-income maximality among allocations feasible under the non-autonomous regime. -/
def MaximizesNonAutonomousLaborIncome
    (d : PropositionSixModel) (e : EquilibriumOutcome) : Prop :=
  ∀ f, d.feasibleNonAutonomous f → f.laborIncome ≤ e.laborIncome

/-- The human occupation sets and wage schedule coincide with their pre-AI values. -/
def CoincidesWithPreAI
    (pre e : EquilibriumOutcome) : Prop :=
  e.aiAssistedWorkers = ∅ ∧
    e.peopleAssistedWorkers = pre.peopleAssistedWorkers ∧
    e.independentProducers = pre.independentProducers ∧
    e.peopleSolvers = pre.peopleSolvers ∧
    e.wage = pre.wage

/--
Proposition 6 (pp. 26--27), including uniqueness, efficiency and labor-income
maximality within the non-autonomous regime, the two AI-use cases, and all four
output/wage comparisons.

The proposition's conclusions are explicit.  The `sourceModelAssumptions`
field does not yet encode the paper's continuous model; this draft Spec is
therefore an incomplete translation, and no theorem below derives it.
-/
def propositionSixSpec : Prop :=
  ∀ d : PropositionSixModel,
    d.sourceModelAssumptions →
    d.aiKnowledge ∈ Set.Ico (0 : ℝ) 1 →
      (∃ e, d.nonAutonomousEquilibrium e) ∧
      (∀ e₁ e₂,
        d.nonAutonomousEquilibrium e₁ →
        d.nonAutonomousEquilibrium e₂ → e₁ = e₂) ∧
      ∀ e,
        d.nonAutonomousEquilibrium e →
          EfficientNonAutonomous d e ∧
          MaximizesNonAutonomousLaborIncome d e ∧
          e.computeRent = 0 ∧
          (d.aiKnowledge ≤ d.preAI.wage 0 → CoincidesWithPreAI d.preAI e) ∧
          (d.preAI.wage 0 < d.aiKnowledge →
            LiesBelow e.aiAssistedWorkers
              (e.peopleAssistedWorkers ∪ e.independentProducers ∪ e.peopleSolvers) ∧
            e.aiAssistedWorkers.Nonempty ∧
            e.peopleAssistedWorkers.Nonempty ∧
            e.peopleSolvers.Nonempty) ∧
          d.autonomousAI.output > e.output ∧
          (∃ z ∈ Set.Ioc (0 : ℝ) 1, e.wage z ≤ d.preAI.wage z) ∧
          (d.preAI.wage 0 < d.aiKnowledge →
            ∃ z ∈ Set.Ioc (0 : ℝ) 1, e.wage z < d.preAI.wage z) ∧
          (∃ ε > (0 : ℝ),
            (∀ z ∈ Set.Ico (0 : ℝ) ε,
              max (d.preAI.wage z) (d.autonomousAI.wage z) ≤ e.wage z) ∧
            (d.preAI.wage 0 < d.aiKnowledge →
              ∀ z ∈ Set.Ico (0 : ℝ) ε,
                max (d.preAI.wage z) (d.autonomousAI.wage z) < e.wage z)) ∧
          (∃ ε > (0 : ℝ),
            (∀ z ∈ Set.Ioc (1 - ε) 1, e.wage z ≤ d.autonomousAI.wage z) ∧
            (∀ z ∈ Set.Ioc (1 - ε) 1,
              z ≠ 1 → e.wage z < d.autonomousAI.wage z))

end

end IT25KnowledgeEconomy
