# Pre-workshop checklist for Workshop 2: Power Tools + Authoring

**Send to attendees between Workshop 1 and Workshop 2.**

---

## Recap

In Workshop 1 we covered the essentials of using Claude Code well: setting up
`CLAUDE.md` as a project-scoped configuration file, understanding the core
primitives (tools, skills, context), and walking through the "superpowers
consumed" workflow — letting Claude select and invoke the right skill for each
task. Workshop 2 builds directly on that foundation. We will extend your
toolbelt by connecting external services through MCPs (Model Context Protocols),
and shift from consuming existing skills to authoring your own, using the
PromptCraft project as a hands-on vehicle.

---

## Required setup (assumes W1 prep is done)

Work through each item before the workshop. Tick them off as you go.

- [ ] **Confirm Claude Code + VSCode extension + superpowers still working from W1**
  Open VSCode, open the Claude Code panel, and send a quick message to confirm
  the setup from Workshop 1 is still intact. If anything has broken since W1,
  re-run the W1 pre-workshop checklist steps.

- [ ] **Clone or update this repo**
  If you do not have the repo locally yet:
  ```
  git clone <repo-url>
  ```
  If you already cloned it, pull the latest changes:
  ```
  git pull origin solution
  ```

- [ ] **Run the PromptCraft app once to verify it works**
  From the repo root:
  ```
  streamlit run promptcraft/app.py
  ```
  The app should open in your browser. If it does not, see the troubleshooting
  FAQ at the bottom of this document.

---

## Optional setup (we'll demo these live; install ahead if you want to follow along)

You do not need to install these before the workshop — we will walk through each
one together. But if you prefer to have them ready, the instructions are below.

- **Context7 MCP**
  Documentation: `<context7-docs-link>`
  Install command:
  ```
  <context7-install-command>
  ```

- **GitHub MCP**
  Documentation: `<github-mcp-docs-link>`
  Install command:
  ```
  <github-mcp-install-command>
  ```
  Authentication setup: after installing, set the `GITHUB_TOKEN` environment
  variable to a personal access token with the scopes your organisation requires.
  See `<org-github-token-guide>` for how to generate and store the token.

---

## For the 90-min bonus (optional)

The extended section of the workshop covers connecting Claude Code to a
Snowflake data warehouse via MCP.

- **Request Snowflake sandbox access from your client or IT team well in
  advance.** Provisioning can take several business days. You will need a
  Snowflake account URL, a warehouse name, and credentials (username + password
  or key-pair auth). Contact `<snowflake-access-contact>` if you are unsure who
  to ask.

- **You do not need to pre-install the Snowflake MCP.** The install will be
  demoed live during the bonus section. Just having credentials ready is enough.

---

## Pre-read (optional)

If you have a few minutes before the workshop, skim:

[guide/02-tutorial.md](../../guide/02-tutorial.md)

This gives background on the PromptCraft project we will extend during the
hands-on portion of W2. No need to read anything else — the workshop is
self-contained.

---

## Troubleshooting FAQ

**Status line not showing / Claude Code not responding**
Start with the W1 troubleshooting steps (reinstall extension, restart VSCode,
check API key). These are the most common causes even in W2.

**MCP not appearing in the tool list**
After installing an MCP, it does not always become available immediately. Restart
your Claude session (close the panel and reopen it, or quit and relaunch VSCode).
If the MCP still does not appear, confirm the install completed without errors.

**MCP authentication errors**
Check that the relevant API key or token environment variable is set in the shell
environment that launched VSCode — not just in a terminal opened after VSCode
started. On macOS and Linux this typically means adding the export to your shell
profile (`~/.zshrc`, `~/.bashrc`) and restarting VSCode from that shell.

**Streamlit fails to start**
Check your Python version — Streamlit requires Python 3.8 or later. If the
`streamlit` command is not found, or you see import errors, install the project
dependencies:
```
pip install -r promptcraft/requirements.txt
```
Then run `streamlit run promptcraft/app.py` again.

**`git pull` fails with merge conflicts**
If you have local changes that conflict with the `solution` branch, stash them
first:
```
git stash
git pull origin solution
git stash pop
```

---

## What to bring on the day

Your laptop with the required setup above completed. If you are joining the
90-min bonus, have your Snowflake credentials to hand.
