# Tutorial: Building PromptCraft With Superpowers

Let's build PromptCraft — a prompt engineering helper — using the superpowers workflow. We'll go through the full process: brainstorming the design, planning the implementation, and building with subagent-driven development.

This isn't a transcript of an actual session, but it's representative of how the workflow feels. The key patterns are real; the specific dialogue is condensed.

---

## Phase 1: Brainstorming the Design

We start with a rough idea: "Build a tool that helps people write better prompts."

That's not a spec. It's a direction. Brainstorming turns it into something we can actually build.

### One Question at a Time

The brainstorming skill doesn't dump a questionnaire on you. It asks one question, waits for your answer, and uses that answer to inform the next question.

**Claude:** "Who will use this tool? Data scientists exploring LLMs, AI engineers building production systems, or general users trying ChatGPT for the first time?"

**You:** "Mostly data scientists and AI engineers. People who already know what prompts are but want to write better ones."

**Claude:** "What kinds of prompts? Simple queries, complex multi-step instructions, system prompts for agents, or all of the above?"

**You:** "Primarily complex instructions — the kind where structure and clarity really matter."

Each question narrows the scope. By the tenth question, we've established:
- The audience (technical users)
- The prompt types (complex instructions)
- The analysis depth (specific, actionable feedback — not generic advice)
- The UI approach (simple Streamlit — focus on the analysis, not the interface)

### Proposing Approaches

Before settling on a design, brainstorming presents options:

**Approach A: Rule-based analysis.** Check for common issues (missing output format, vague verbs, no examples) using pattern matching. Fast, predictable, but limited.

**Approach B: LLM-based analysis.** Have Claude analyze the prompt and suggest improvements. Flexible, nuanced, but slower and less predictable.

**Approach C: Hybrid.** Rule-based checks for obvious issues, LLM analysis for deeper feedback. Best of both worlds, more complexity.

Each approach comes with trade-offs. Rule-based is faster to build but less capable. Full LLM is more powerful but harder to test. Hybrid is the most capable but takes longer.

For PromptCraft, we choose **Approach C (hybrid)**. The rule-based layer catches obvious issues immediately; the LLM layer provides nuanced suggestions.

### The Validated Design

By the end of brainstorming, we have:

- **Core features:** Input area, rule-based analysis, LLM-based suggestions, refined output display
- **UI framework:** Streamlit (simple, data-science-friendly)
- **Analysis approach:** Hybrid (rules + LLM)
- **Excluded (YAGNI):** Prompt history, multiple LLM providers, user accounts

This isn't a vague direction anymore. It's a design we can implement.

**Key takeaway:** We haven't written a line of code, but we've already avoided the biggest risks — building the wrong thing, over-engineering, scope creep. The brainstorming skill made us answer hard questions before they became expensive.
