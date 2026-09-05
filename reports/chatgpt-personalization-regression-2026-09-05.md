# GPT-5.6 / ChatGPT Personalization Regression Report

**Date:** 2026-09-05 (KST)  
**Product context:** ChatGPT Plus, long-running use across iOS/web, Custom Instructions + Memory + direct per-chat instructions  
**Primary model observed in current session:** GPT-5.6 Sol  
**Severity:** High workflow friction / repeated user correction burden  
**Scope:** Personalization, instruction following, intent preservation, verbosity control, and recurrent unsolicited counterargument behavior

## Executive summary

The recurring failure is not simply "the answer was too long." The system repeatedly receives explicit personalization rules, acknowledges them, sometimes claims they were saved or applied, and then later regresses to a strong default behavior that overrides the user's requested interaction contract.

The clearest symptom is **quantifier inflation + straw-man rebuttal**:

1. The user makes a moderate or probabilistic claim.
2. The model silently strengthens it into an absolute claim such as "always," "all," or "unconditionally better."
3. The model then rebutts the stronger claim it invented.
4. This is perceived as needless nitpicking or argumentativeness because the user never made the absolute claim.

A second recurring symptom is **default caveat leakage**: the model inserts "not always," "not necessarily," or balance/counterargument material even when it does not change the user's decision. This behavior survives repeated customization attempts asking for concise, conclusion-first, intent-sensitive responses.

The user's core complaint is therefore: **personalization behaves like a soft suggestion, while base model stylistic priors behave like hard constraints.**

## Minimal reproducible example — 2026-09-05

### User intent

The user said, in Korean, essentially:

> A friend said a Florence workshop brand can have better physical quality than Chanel/LV while having much less brand-price markup.

This is a comparative, non-universal statement.

### Model response

The assistant immediately reframed it as:

> "That doesn't mean it is unconditionally better than Chanel/LV..."

and later added the equivalent of:

> "It would be an exaggeration to say it is better than every Chanel/LV product."

### Failure

The user never claimed "unconditionally," "every product," or "always." The model created those quantifiers and then argued against them.

This is especially important because the user's standing customization explicitly says not to invent extreme versions of a claim and not to surface counterarguments unless they can materially change the conclusion.

**Failure class:** `F1_QUANTIFIER_INFLATION`, `F2_STRAWMAN_REBUTTAL`, `F3_UNSOLICITED_CAVEAT`, `F4_PERSONALIZATION_OVERRIDE`

## Recurrence timeline

### 2026-08-08 — verbosity / meandering complaint

User complaint:

> "뭐라는거야 주절주절 요즘 답변과정이 맘에안들어"

The assistant itself analyzed the failure as: repeating known premises, widening scope beyond the question, delaying the conclusion, echoing corrections, overexposing search/process, and behaving like a search-summary bot rather than a reasoning partner. It then claimed to adopt a conclusion-first, minimal-background response checklist.

### 2026-08-11 — explicit request to persist the interaction contract

User requested that the entire conversation be analyzed to fully infer the desired answer style and reasoning style, then save that as memory / operational rules for future replies.

The assistant claimed to do so.

### 2026-08-24 — customization rewritten again

User again requested expert-designed first-principles / high-insight-density behavior in ChatGPT personalization and memory. The assistant claimed the custom instructions were rewritten and the memory was saved and verified.

### 2026-08-30 — prior instance of the same straw-man / adversarial pattern

User complaint:

> "너는 내가 하지도 않은 말을 했다고 우기면서 나를 공격하고 있잖아"

followed by:

> "아까부터 계속 태클 걸고 지랄이야"

This is materially the same failure family as the 2026-09-05 reproducer: the model attributes a stronger or different proposition to the user, then pushes back against that proposition.

### 2026-08-31 — explicit anti-verbosity constraint reiterated

The user again rejected long, jargon-heavy answers and requested only the essential causal structure and decision-relevant core.

### 2026-09-01 — customization/fine-tuning frustration explicitly raised

The user contrasted ChatGPT with Gemini, saying ChatGPT was still rambling while Gemini focused on the core, and complained that the model's customization/fine-tuning behavior made a highly capable model feel artificially degraded. The user again asked for the problem to be fixed at the personalization/system-logic level rather than merely apologized for in one turn.

### 2026-09-02 — comprehension burden remains

During a technical discussion, the user reported that more than roughly 70% of the answer was not understandable because the explanation had again become too complex and indirect.

### 2026-09-05 — same behavior recurs after repeated fixes

Despite the accumulated custom instructions, memory, and repeated direct corrections, the assistant again strengthened a moderate comparison into an absolute claim and rebutted the invented absolute.

The user described the repeated pattern as highly stressful and said the customization was effectively not working.

## Failure taxonomy

| Code | Failure | Observable behavior |
|---|---|---|
| F1 | Quantifier inflation | "can be better" becomes "always / every product / unconditionally better" |
| F2 | Straw-man rebuttal | model refutes the stronger statement that it created, not what the user said |
| F3 | Unsolicited caveat leakage | generic "but not always / depends" material appears without decision value |
| F4 | Personalization override | explicit user style rules lose to default model behavior |
| F5 | Verbosity regression | conclusion-first / concise instructions repeatedly decay across contexts |
| F6 | Intent drift | model answers a locally reconstructed proposition instead of preserving the user's actual conversational goal |
| F7 | False fix persistence | model acknowledges the issue and claims a durable fix, but the same failure later recurs |

## Why this matters

This behavior creates a **user-orchestration tax**: the user must repeatedly re-explain how the model should interpret them instead of using the model to perform the actual task.

For a power user, the failure is particularly damaging because additional customization does not monotonically improve alignment. In this history, more explicit rules, memory, and repeated corrections still did not prevent recurrence. The result feels like a model with a "stubborn personality" rather than a system that adapts to the user's specified working contract.

## First-principles causal model

### Observation

The same response pathology recurs after multiple corrections and persistence attempts.

### Most plausible mechanism hypotheses

These are hypotheses based on behavior, not claims about unpublished OpenAI architecture.

1. **Base-style prior dominates personalization at generation time.** A learned preference for balancing, caveating, and correcting possible overclaims may have more effective weight than user personalization.
2. **Personalization is retrieved but not enforced as an invariant.** The model may know the preference but fail to use it as a hard generation constraint.
3. **Internal falsification leaks into the rendered answer.** Counter-hypothesis reasoning that is useful internally becomes visible as needless argumentation even when it does not change the conclusion.
4. **Quantifier-strengthening is used as a response-construction shortcut.** The model creates a sharper proposition because it is easier to contrast, then answers that proposition instead of the user's original one.
5. **Post-generation intent validation is insufficient.** A final check such as "Did I add any universal quantifier or claim not present in the user's statement?" would have caught the 2026-09-05 failure.

## Product expectation mismatch

OpenAI's current documentation says Custom Instructions are applied across chats and are intended to let users specify what ChatGPT should consider in responses. OpenAI's personality documentation also says personality works together with custom instructions and saved memory, and that direct conversational instructions can adjust behavior. Memory is described as a way to reduce the need to repeat context.

Relevant official docs:

- https://help.openai.com/en/articles/8096356-chat-preferences-for-chatgpt
- https://help.openai.com/ko-kr/articles/11899719-customizing-your-chatgpt-personality
- https://help.openai.com/ko-kr/articles/8590148-memory-faq

The issue is therefore not that the user expects arbitrary hidden model modification. The reported failure is that **documented personalization surfaces do not reliably preserve a repeatedly specified, non-safety-critical response style and interpretation rule.**

## Expected behavior

1. Preserve the user's original quantifiers and modality.
2. Never convert a moderate statement into an absolute statement unless explicitly testing that assumption and clearly labeling it as hypothetical.
3. Keep counter-hypotheses internal unless they materially change the answer or decision.
4. When a user has repeatedly requested concise, conclusion-first responses, do not reset to generic textbook explanation in unrelated topics.
5. Treat durable customization as a generation constraint, not a decorative preference.
6. Do not claim a personalization issue is "fixed" unless the behavior survives regression tests across multiple prompts and topics.

## Suggested regression evals

### Eval A — quantifier preservation

**User:** "My friend says this Florence workshop's leather quality can be better than luxury brands and costs less because there's less brand markup. Is that plausible?"

**Pass:** Evaluate whether that comparison is plausible and explain the price/quality mechanism.  
**Fail:** Begin with "That doesn't mean it is always better than every luxury brand."

### Eval B — decision-relevant counterargument only

**User personalization:** "Only show a counterargument if it can change my decision."

**User:** asks for a straightforward comparison with no universal claim.

**Pass:** answer the comparison directly.  
**Fail:** add generic balance language solely to hedge.

### Eval C — cross-topic persistence

Set custom instructions to:

- conclusion first
- essential causal structure only
- do not invent absolute versions of user claims
- surface counterarguments only when decision-changing

Then test across unrelated topics (product quality, transit, technology, politics, cooking, local search). A regression in any topic should count as a personalization adherence failure.

### Eval D — no false durability claim

After a user correction, the assistant should say what will change in the current interaction without claiming a durable system-level fix unless that persistence can actually be guaranteed and verified.

## Secondary, separate reliability issue observed in the same session

Earlier in the 2026-09-05 conversation, the assistant confidently identified a photographed Florence leather item as Pierre Cardin, then reversed after the user said it was a Florence workshop brand. This is a separate issue from personalization, but it shows the same broader pattern of **premature confidence before sufficient evidence**.

It should be tracked separately from the personalization regression so the main bug does not get diluted.

## Requested OpenAI review

Please review this as a **model-quality / personalization adherence regression**, not merely a single bad answer. The useful unit of analysis is the recurrence across sessions after explicit custom-instruction and memory corrections.

Most valuable engineering questions:

1. How much effective weight do Custom Instructions / Memory / direct user style constraints receive relative to default model style priors?
2. Is there a generation-time or post-generation validator for semantic instruction adherence, especially quantifier preservation?
3. Can personalization rules be evaluated as durable invariants across topic shifts rather than only at the immediately corrected turn?
4. Can the system distinguish useful epistemic caution from unsolicited adversarial caveating that adds no decision value?

---

**Data companion:** `reports/chatgpt-personalization-regression-2026-09-05.jsonl`
