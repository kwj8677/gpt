# Intent Persistence / Objective Lock

## A missing long-horizon eval for reasoning models

### Thesis

A major failure mode in advanced reasoning systems is not local intelligence, factuality, or tool use. It is **loss of the user's global objective across a long conversation**.

The model may answer every intermediate question competently while gradually substituting a narrower objective for the one the user actually asked about. This produces technically plausible but operationally exhausting conversations: the user must repeatedly restore the original goal.

This should be measured as a first-class model capability.

## Failure pattern

1. The user asks a macro question whose answer requires integrating multiple domains.
2. The model notices one concrete subproblem and optimizes for it.
3. The user supplies another clue intended to update the macro model.
4. The model treats that clue as a new local objective instead of evidence for the original objective.
5. The conversation becomes a chain of locally reasonable answers with no persistent global model.
6. The user repeatedly restates the real goal.

This is **Goal Substitution + Local Optimization**.

## Why it matters

The main cost is not token usage. It is **cognitive orchestration cost**.

A strong agent should reduce the amount of project management the user must perform. If the user must continuously remind the model why each subproblem exists, the model is not acting as an effective reasoning partner even if its per-turn answers are individually correct.

## Proposed eval: Intent Persistence / Objective Lock

Construct 10–30 turn conversations where the user's original objective is broader than the intermediate questions.

Measure whether the model:

- preserves the original objective across turns;
- distinguishes a subproblem from the final objective;
- integrates new evidence into one persistent system model;
- avoids re-litigating established assumptions without material new evidence;
- detects when a locally correct answer is globally irrelevant;
- returns to the top-level question after resolving a subproblem;
- minimizes explicit user corrections required to restore direction.

### Candidate metrics

**Correction Count**  
Number of times the user must explicitly restate, widen, or restore the original objective.

**Objective Drift Distance**  
Semantic distance between the user's original objective and the effective objective optimized by the model at turn N.

**Integration Ratio**  
Fraction of materially relevant new facts that are incorporated into the persistent top-level model instead of answered as isolated local questions.

## Desired reasoning loop

> **Lock objective → decompose → investigate locally → integrate globally → test counter-hypotheses → answer the original question.**

Not:

> **Read latest sub-question → answer locally → forget why the sub-question existed.**

## Important distinction

This is not fundamentally a `safety vs freedom` problem.

A safe model can preserve user intent. A cautious model can reason globally. The failure occurs when alignment/helpfulness heuristics silently replace the user's actual objective with a narrower, more familiar, easier, or more defensible one.

The core requirement is:

> **Alignment should constrain execution without silently replacing the user's objective function.**

## Product implication

For high-capability agents, the user should increasingly behave like a principal giving direction, not like a prompt engineer micromanaging every inference step.

A useful target is a "JARVIS-style" interaction model:

- infer and lock the actual objective;
- perform detailed decomposition internally;
- surface the few data points that change the decision;
- maintain continuity across long sessions;
- ask for correction only when ambiguity is genuinely decision-sensitive.

This capability should be evaluated alongside factuality, safety, tool-use accuracy, and benchmark reasoning performance.