# Rehearsal Checklist and Risk Register

## Purpose

Dry-running workshops before delivery ensures that timing is calibrated, demos work end-to-end in the actual environment, and every fallback path has been exercised at least once. "Rehearsed" in this context means: a presenter has run each demo from the exact starting state described in the demo script, measured wall-clock time against the session budget, and verified that every fallback asset (screenshot, recording, narration) is ready and accessible.

Skipping dry runs risks live demo failures with no prepared response, timing overruns that cut Q&A or the bonus section, and presenters discovering environment issues (missing dependencies, auth errors, network blocks) in front of attendees.

## One-week-before checklist

- [ ] Confirm presenters and roles: who delivers W1 vs. W2, who handles each demo section, who manages the room/chat.
- [ ] Confirm pre-workshop materials have been sent to all registered attendees: `pre-workshop-w1.md` for Workshop 1 cohort, `pre-workshop-w2.md` for Workshop 2 cohort.
- [ ] Confirm Snowflake sandbox is provisioned for the W2 90-min bonus. If not provisioned, plan the fallback per the W2 bonus risk register (slides-only walkthrough of the hook pattern).
- [ ] Confirm API key budget is cleared and sufficient for all live demos across both workshops (including exploratory queries attendees may run).
- [ ] Confirm recording and streaming setup if the session will be recorded or broadcast: camera, screen capture software, stream key.
- [ ] Confirm venue logistics: room booking, projector or screen resolution, microphone/speaker setup, and stable network connectivity (including whether the venue blocks external API calls).

## Three-days-before — full dry run

- [ ] Run W1 end-to-end: theory part 1, Demo 1, theory part 2, Demo 2. Log actual elapsed times against the session budget and note any overruns.
- [ ] Run W2 end-to-end: theory part 1, Demo 1, theory part 2, Demo 2. Log actual elapsed times.
- [ ] For every demo, capture a backup screen recording of a successful run so it can be played if the live attempt fails.
- [ ] For W1 Demo 2: verify that the visual companion offer triggers reliably using the magic prompts in `docs/superpowers/workshops/magic-prompts.md` §3. If it does not trigger consistently, either tune the steering question or commit to the fallback narration path before delivery day.
- [ ] For W2 Demo 1: capture a screenshot pair showing the vanilla (no Context7) query result alongside the Context7-enhanced result as a backup contrast asset.
- [ ] Capture the W1 Demo 1 `/init` output as a screenshot to use as the fallback described in `docs/superpowers/workshops/workshop-1/demo-1-script.md`.
- [ ] Capture the W2 Demo 2 trigger output as a screenshot fallback for the skill auto-invocation moment.

## Day-of checklist

- [ ] VSCode windows pre-arranged and at the exact starting state described in each demo's setup section before attendees arrive.
- [ ] Browser tabs for the visual companion already open and positioned.
- [ ] All relevant branches checked out and verified clean: `master`, `solution`, `workshop-w1-demo`, `workshop-w2-demo`.
- [ ] Confirm Streamlit can launch without errors: `streamlit run promptcraft/app.py`.
- [ ] All MCPs that demos rely on (not ones installed live during the demo) are already authenticated and responding.
- [ ] Phone on silent. Desktop notifications muted on all presenter machines.
- [ ] Backup screen recordings confirmed accessible — either in cloud storage (link tested) or on local disk.

## Risk register — consolidated

| Workshop | Failure mode | Likelihood | Fallback |
|---|---|---|---|
| W1 Demo 1 | `/init` produces unexpected or malformed output | Medium | Show pre-captured screenshot of expected output; narrate what it should contain |
| W1 Demo 1 | Plan mode UI not visible in VSCode | Low | Toggle plan mode via CLI flag; if still hidden, narrate the plan from terminal output |
| W1 Demo 1 | Checkpoint revert doesn't restore state | Low | Manually restore from the `workshop-w1-demo` branch; narrate the revert concept |
| W1 Demo 2 | Brainstorm doesn't ask the UI question | Medium | Use the steering question from `magic-prompts.md` §3 to redirect; if still absent, narrate the expected exchange |
| W1 Demo 2 | Visual companion not offered by Claude | Medium | Use the magic prompt trigger; if unreliable, switch to fallback narration and describe what would appear |
| W1 Demo 2 | Streamlit fails to start | Low | Show the pre-captured recording of the app; describe the UI live |
| W1 Demo 2 | Brainstorm conversation derails | Medium | Paste the pre-written steering prompt; reset to a clean context window |
| W1 90-min bonus | Claude patches the bug instead of re-brainstorming | Medium | Explicitly prompt Claude to treat the change as a new requirement; narrate the expected re-brainstorm pattern |
| W1 90-min bonus | Subagent dispatch not visible in UI | Low | Show terminal output; narrate what the subagent coordination looks like |
| W2 Demo 1 | Context7 install fails | Medium | Use the pre-installed fallback environment; demonstrate from screenshots if install is blocked |
| W2 Demo 1 | Vanilla query returns an accurate/current answer | Medium | Switch to a query that is known to return stale results in the vanilla path; use the pre-captured screenshot pair |
| W2 Demo 1 | Streamlit fails to start | Low | Show the pre-captured recording; narrate the UI |
| W2 Demo 2 | Skill not auto-invoked by Claude | Medium | Manually invoke with the explicit slash command; narrate the expected auto-detection behavior |
| W2 Demo 2 | Status line doesn't show skill name | Low | Show the pre-captured screenshot fallback; explain what the status message should read |
| W2 Demo 2 | Live editing of the skill breaks execution | Low | Revert to the last working version from the `workshop-w2-demo` branch |
| W2 90-min bonus | Snowflake sandbox unavailable | High | Deliver slides-only walkthrough of the hook pattern; skip live execution |
| W2 90-min bonus | Hook script fails to load | Medium | Show the pre-captured recording of a successful hook trigger; narrate the configuration |
| Any | Demo derails entirely | Low | Pivot to slides and narrate the backup recording |

## Live-pivot decisions

**W1 theory part 1 running long:** Drop the "Permissions" topic to a single-sentence mention ("Permissions are configurable — see the docs") and move on. Do not attempt to compress it; compressed explanations of permissions create confusion.

**W1 theory part 2 running long:** Merge the "writing-plans" and "subagent-driven development" segments into a single pass. Present them as one continuous workflow rather than two discrete topics.

**Demo 1 (either workshop) runs long:** Skip the setup explanation for Demo 2 and go straight into the live execution. Attendees can read the setup steps in the demo script; they do not need a narrated walkthrough of environment prep.

**90-min bonus unwanted by the audience:** Cut the bonus early. End at the 60-minute mark, open Q&A, and offer to share the bonus material asynchronously. Do not push bonus content on an audience that has signaled disengagement.

## Post-workshop

- [ ] Capture all audience questions that were not answered during the session and add them to the FAQ backlog.
- [ ] Note which demos ran smoothly and which hit live issues; record this before leaving the venue.
- [ ] Update `magic-prompts.md` if any prompt needed live tuning during the session — record the tuned version immediately while it is fresh.
- [ ] Send a brief survey to attendees asking which topics they would want deeper coverage of in a follow-up session.
