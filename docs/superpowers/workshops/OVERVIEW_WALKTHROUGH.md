# Workshops Walkthrough Guide

A prioritized reading order for walking a co-presenter, reviewer, or new team member through the workshops content. Use this as your agenda for a 1-on-1 walkthrough session.

**Start by pairing with:** [OVERVIEW.md](OVERVIEW.md) — the condensed content summary this guide sequences around.

---

## Tier 1 — Start here (~10 min)

Fast orientation. Get the shape of the whole thing before drilling into any one artifact.

1. **[OVERVIEW.md](OVERVIEW.md)** — the whole workshop story in one read. Audience, format, W1/W2 topics, demos, capability coverage, deliverables, status.
2. **[Design spec](../specs/2026-04-15-claude-code-workshops-design.md)** — only dip in for the *why* behind specific choices (core narrative, capability bucketing rationale, live-pivot option, open questions). Skip sections OVERVIEW already covers.

---

## Tier 2 — The actual content (~30 min)

Walk the slides side-by-side with your coworker. This is where they get a mental model of what each workshop covers minute-by-minute.

3. **[workshop-1/slides.md](workshop-1/slides.md)** — slide-by-slide spec. Each slide's title, body bullets, speaker notes, demo cues, and time markers.
4. **[workshop-2/slides.md](workshop-2/slides.md)** — same for W2.
5. **[slide-3-rewrite.md](slide-3-rewrite.md)** — short (32 lines). Re-bucketed capabilities diagram that replaces slide 3 of the existing pptx. Flag early — it reframes the whole deck.

---

## Tier 3 — How to present (~25 min)

The talking points. Essential if your coworker will co-present or provide delivery feedback.

6. **[workshop-1/presenter-script.md](workshop-1/presenter-script.md)** — full prose talking points for each W1 slide.
7. **[workshop-2/presenter-script.md](workshop-2/presenter-script.md)** — same for W2.

---

## Tier 4 — Demos (skim; deep-dive the ones they'll own)

Four main demos + two bonus (90-min) demos. Have your coworker pick which they'd own, then deep-dive those together.

8. **[workshop-1/demo-1-script.md](workshop-1/demo-1-script.md)** — primitives-in-action (CLAUDE.md, plan mode, checkpoints)
9. **[workshop-1/demo-2-script.md](workshop-1/demo-2-script.md)** — brainstorm-and-reveal (PromptCraft live + cooked-turkey pivot)
10. **[workshop-1/bonus-demo-script.md](workshop-1/bonus-demo-script.md)** — the curveball + Q&A (90-min)
11. **[workshop-2/demo-1-script.md](workshop-2/demo-1-script.md)** — Context7-in-PromptCraft
12. **[workshop-2/demo-2-script.md](workshop-2/demo-2-script.md)** — custom skill authoring (~15-line SKILL.md)
13. **[workshop-2/bonus-demo-script.md](workshop-2/bonus-demo-script.md)** — Snowflake MCP + safety hook (90-min)
14. **[magic-prompts.md](magic-prompts.md)** — engineered "magic prompts" for the W1 Demo 2 brainstorm seed + visual companion trigger, with fallbacks.

---

## Tier 5 — Logistics and rehearsal (~15 min)

What attendees need before they show up, and how to dry-run without surprises.

15. **[pre-workshop-w1.md](pre-workshop-w1.md)** — pre-W1 attendee setup: Claude Code CLI, VSCode extension, superpowers install, verification.
16. **[pre-workshop-w2.md](pre-workshop-w2.md)** — pre-W2 setup: Context7/GitHub MCP install, Snowflake sandbox credentials.
17. **[rehearsal-checklist.md](rehearsal-checklist.md)** — dry-run steps, risk register, failure modes and fallbacks.

---

## Suggested session structures

### For a 60-min walkthrough

- **10 min:** OVERVIEW + design spec dip (Tier 1)
- **25 min:** W1 slides + presenter script side-by-side (Tiers 2 & 3, W1 half)
- **20 min:** Same for W2
- **5 min:** Point at demo scripts, pre-workshop, rehearsal as follow-up reading

### For a 90-min walkthrough (more demo focus)

- **10 min:** OVERVIEW + design spec dip
- **20 min:** W1 slides + presenter script
- **15 min:** W1 demos walkthrough (at least Demo 2, the PromptCraft reveal)
- **20 min:** W2 slides + presenter script
- **15 min:** W2 demos walkthrough
- **10 min:** Pre-workshop + rehearsal checklist + Q&A

### For co-presenter preparation (multi-session)

- **Session 1 (60 min):** Tiers 1–3 — full content orientation
- **Session 2 (60 min):** Tier 4 — deep-dive the demos they'll own, dry-run together
- **Session 3 (30 min):** Tier 5 — pre-workshop logistics + final rehearsal walkthrough

---

## Shortcuts by role

**Partner reviewer** (approving content): Tiers 1 + 2 only. ~40 min.

**Reviewer of a specific demo:** OVERVIEW + relevant demo script + rehearsal checklist entry for that demo. ~15 min.

**Co-presenter taking one workshop:** Tiers 1–5 but only their workshop's files. ~75 min.

**Attendee support lead** (fielding setup questions): OVERVIEW + pre-workshop-w1.md + pre-workshop-w2.md + rehearsal-checklist.md risk register. ~20 min.

---

## Related reference

- **Companion resources** (NotebookLM demo notebook, slide-deck generation prompt): see [OVERVIEW.md § Companion resources](OVERVIEW.md#companion-resources)
- **Current status** (paused after Task 17 awaiting partner review): see [OVERVIEW.md § Current status](OVERVIEW.md#current-status)
