# NotebookLM Authentication Setup

This document explains how to authenticate the NotebookLM synthesis workflow for case study extraction.

**Status:** Authentication required before synthesis can run

**Location of synthesis script:** `docs/synthesis-workflow.py`

---

## Quick Authentication (5 minutes)

### Method 1: Using notebooklm-mcp-auth (Recommended)

This is the easiest approach. The auth tool handles Chrome DevTools extraction automatically.

```bash
cd ~/.claude/notebooklm-mcp
source venv/bin/activate
notebooklm-mcp-auth --file
```

This will guide you through:
1. Opening Chrome DevTools
2. Finding a NotebookLM network request
3. Copying the cookie header
4. Saving it to a file

The tool then extracts CSRF token and session ID automatically.

### Method 2: Manual Chrome DevTools Extraction

If the above doesn't work:

1. Open `https://notebooklm.google.com/` in Chrome
2. Press F12 (DevTools)
3. Go to **Network** tab
4. Do anything in NotebookLM (create notebook, ask question, etc)
5. Find request: `batchexecute`
6. Click it → **Headers** section
7. Copy the `Cookie:` header value
8. Run:
   ```bash
   cd ~/.claude/notebooklm-mcp && source venv/bin/activate
   notebooklm-mcp-auth --file ~/cookies.txt
   ```

---

## Authentication Verification

After running `notebooklm-mcp-auth`, verify it worked:

```bash
cd ~/.claude/notebooklm-mcp && source venv/bin/activate
python3 << 'EOF'
import json
from pathlib import Path

auth_file = Path.home() / '.notebooklm-mcp' / 'auth.json'
if auth_file.exists():
    auth = json.load(open(auth_file))
    print(f"✓ Auth cached: {len(auth['cookies'])} cookies")
    print(f"✓ Saved at: {auth['extracted_at']}")
else:
    print("✗ No auth cached yet")
EOF
```

---

## Using the Synthesis Workflow

Once authenticated, run:

```bash
cd /home/peter/homelab/projects/active/petersalvato.com
python3 docs/synthesis-workflow.py savepoint-protocol
```

This will:
1. Load manifest entry for the project
2. Load extraction timeline
3. Create NotebookLM notebook
4. Add both sources
5. Query for narrative synthesis
6. Write outline to `docs/working/outline-savepoint-protocol.md`

---

## Authentication Token Expiration

NotebookLM tokens expire periodically. If you see:

```
Authentication expired. Run 'notebooklm-mcp-auth' in your terminal
```

Simply re-authenticate:

```bash
cd ~/.claude/notebooklm-mcp && source venv/bin/activate
notebooklm-mcp-auth --file
```

It's a 2-minute process.

---

## Troubleshooting

### "No cached auth tokens"

The synthesis script couldn't find authentication.

**Solution:** Run `notebooklm-mcp-auth --file` as described above.

### "Authentication expired"

Your cached tokens expired.

**Solution:** Re-run `notebooklm-mcp-auth --file` to refresh.

### "Invalid CSRF token"

The tokens became invalid (cookie session ended).

**Solution:** Re-run `notebooklm-mcp-auth --file` with fresh cookies from Chrome DevTools.

### Script hangs during "Adding sources"

NotebookLM is processing large files. Wait 30-60 seconds.

If it times out, the timeline may be too large. Split it:
- Edit timeline to extract first 5000 lines
- Run synthesis on excerpt
- Repeat with different sections if needed

---

## Files Reference

- **Synthesis script:** `docs/synthesis-workflow.py`
- **Auth config:** `~/.notebooklm-mcp/auth.json` (auto-generated)
- **Cached cookies:** `~/.claude/.notebooklm-creds/cookies.txt` (optional backup)
- **MCP installation:** `~/.claude/notebooklm-mcp/`

---

## Integration with Specialist Workflow

### Timeline Narrator Specialist

The Timeline Narrator Specialist runs:

```bash
python3 docs/synthesis-workflow.py [project-slug]
```

**Input:**
- Project slug (e.g., `savepoint-protocol`, `aiden-jae`)
- Manifest entry (auto-loaded from mainfest.json)
- Extraction timeline (auto-loaded from docs/extraction_timelines/)

**Output:**
- `docs/working/outline-[project].md` (structured narrative arc with synthesis)

**Time:** 2-3 minutes per project (NotebookLM processing time)

**Auth:** Must be pre-configured (one-time setup, then lasts days)

### Master Builder Copywriter Specialist

After Timeline Narrator completes, Master Builder receives:
- Context spec (`docs/working/context-[project].md`)
- Timeline outline (`docs/working/outline-[project].md`)

Master Builder writes the case study using these as source material.

---

## Authentication for Next Week (When Tokens Refresh)

When you start the next rebuild session:

1. Run `notebooklm-mcp-auth --file` once (5 minutes)
2. Use synthesis script for all 8 projects
3. Auth stays cached for ~1 week

No additional setup needed during the week.

---

## Why This Approach?

**Direct API:** Would require rebuilding all auth handling ourselves
**MCP:** Adds complexity for what is essentially a batch pipeline
**Wrapped MCP:** Best of both worlds - uses proven auth, exposes simple CLI interface

The synthesis-workflow.py script is a thin wrapper that:
- Handles auth transparently
- Loads project data automatically
- Runs NotebookLM synthesis
- Outputs structured outline
- Can be called by agents or humans

Result: Timeline Narrator Specialist just runs one command per project.
