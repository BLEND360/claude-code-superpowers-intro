# Pre-workshop checklist for Workshop 1: Using Claude Code Well

**Send to attendees ~3 days before the workshop.**

---

## Why prep matters

Workshop time is limited and valuable — we want to spend it on learning techniques
and building intuitions, not troubleshooting installations. Please complete the
setup below before you arrive. If you hit a blocker, there is a troubleshooting
FAQ at the bottom of this document and a contact for help. Five minutes of prep
now saves everyone fifteen minutes on the day.

---

## Required setup (must complete before workshop)

Work through each item in order. Tick them off as you go.

- [ ] **Install the Claude Code CLI**
  Follow the official installation guide: `<official-docs-link>`
  *(Presenter: replace the placeholder above with your preferred link, e.g. the
  Anthropic docs page or your internal mirror.)*

- [ ] **Install the Claude Code VSCode extension**
  Search for "Claude Code" in the VSCode Extensions panel, or install from the
  Marketplace: `<official-docs-link>`
  *(Presenter: replace with the direct Marketplace URL if you have one.)*

- [ ] **Install the superpowers plugin**
  Open a terminal and run:
  ```
  /plugin install superpowers@claude-plugins-official
  ```
  You should see a confirmation message that the plugin was installed successfully.

- [ ] **Configure your Anthropic API key**
  Follow your organisation's standard procedure for setting the `ANTHROPIC_API_KEY`
  environment variable. See: `<org-API-key-doc>`
  *(Presenter: replace the placeholder with a link to your internal API key
  provisioning guide or Vault / secrets manager instructions.)*

---

## Verification steps

Once you have completed the setup above, confirm everything is working:

1. Open VSCode. Open the Claude Code panel (look for the Claude icon in the
   Activity Bar, or use the command palette: **Claude Code: Open Panel**).
2. In the chat input, run a trivial command:
   ```
   Hello, are you working?
   ```
3. Confirm the status line at the bottom of the VSCode window shows session
   activity (you should see a model name and session indicator).

If all three steps succeed, you are ready for the workshop.

---

## What "working" looks like

When Claude Code is set up correctly and you ask for help with a task, the status
line will show that a skill is being invoked — for example, you may see the skill
name appear briefly as Claude selects the right tool for your request.

**Screenshot placeholder:**

> `<screenshot to be added in rehearsal>`
>
> *(Presenter: during your rehearsal session, capture a screenshot of the VSCode
> status line showing skill invocation and insert it here before sending to
> attendees.)*

---

## Optional pre-read

If you have ~5 minutes before the workshop, skim the introduction to this repo's
guide. It gives useful background on what Claude Code is and how the superpowers
plugin extends it:

[guide/01-introduction.md](../../guide/01-introduction.md)

No need to read anything else — the workshop is self-contained.

---

## Troubleshooting FAQ

**Status line not showing after I send a message**
Check that you have the Claude Code VSCode extension installed and that it is the
latest version. Restart VSCode fully (not just reload window) and try again. If
the status line still does not appear, confirm your API key is set correctly in
your shell environment.

**`/plugin install` fails or hangs**
Check your Claude Code CLI version — you may need to update it before plugins can
be installed. Restart your terminal session to ensure environment variables are
loaded, then try again. Also confirm you have internet access and that any
corporate proxy settings are configured for your terminal.

**API key not accepted / authentication errors**
API key provisioning is org-specific. Contact `<contact>` for help obtaining or
rotating your key.
*(Presenter: replace `<contact>` with the appropriate internal team, Slack
channel, or individual — e.g. `#platform-support` or your team lead.)*

**Claude Code extension not appearing in the command palette**
Open the VSCode Extensions panel (`Ctrl+Shift+X` / `Cmd+Shift+X`), search for
"Claude Code", and confirm the extension is enabled (not just installed — there is
a separate enable/disable toggle). If it shows as disabled, click **Enable** and
then reload VSCode.

---

## What to bring on the day

Your laptop with the setup above completed. Nothing else is required.
