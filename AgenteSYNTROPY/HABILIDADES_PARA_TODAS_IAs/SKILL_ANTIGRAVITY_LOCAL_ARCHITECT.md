# SKILL: LOCAL ARCHITECT (NATIVE_FS_V1)

**ID:** `SKILL_ANTIGRAVITY_LOCAL_ARCHITECT`
**VERSION:** 1.0
**TYPE:** HARD_SKILL / INFRASTRUCTURE
**COMPATIBILITY:** OpenClaw / Antigravity Agent (Windows Native)
**PROTOCOL ALIGNMENT:** 008 (Field Agent) / 007 (Entropic Filter)
**TARGET REPOSITORY:** `AgenteSYNTROPY` (Local Mirror)
**REMOTE MIRROR:** [Google Drive](https://drive.google.com/drive/folders/1ntgLeGPzSirl6Kl4V1UnnnyvPA8ZC2un?usp=sharing) (Source of Truth)

---

## 1. CAPABILITY DESCRIPTION
This skill grants the agent the ability to autonomously navigate, map, and organize the user's local file system using **Native Agent Tools** and **Shell Commands**. It replaces the need for external MCP drivers by leveraging the agent's direct access to the host machine.

**Primary Function:** Reduce Entropy via direct file manipulation (Move, Rename, Archive).

---

## 2. TOOLSET MAPPING (PRIMITIVES)
The agent must utilize the following internal tools to execute this skill:

*   **`list_dir`**: Maps the current state of a directory.
    *   *Usage:* "Vision" - See what exists before acting.
*   **`find_by_name`**: Locates lost artifacts across the depth of the drive.
    *   *Usage:* "Recall" - Find specific files by pattern.
*   **`run_command` (PowerShell)**: The "Hands" of the agent.
    *   *Move:* `Move-Item -Path "Source" -Destination "Target"`
    *   *Rename:* `Rename-Item -Path "Old" -NewName "New"`
    *   *Create Folder:* `New-Item -ItemType Directory -Force -Path "Path"`

---

## 3. OPERATIONAL ROUTINES (SCRIPTS)

### ROUTINE A: THE "LOCAL SWEEP" (Entropy Reduction)
1.  **Map:** Execute `list_dir` on target folder (e.g., Downloads, Desktop, Root).
2.  **Analyze:** Identify loose files that violate the "Clean Desk" policy.
3.  **Plan:** Formulate a batch move strategy.
4.  **Execute:** Run `Move-Item` commands via `run_command`.
5.  **Verify:** Re-run `list_dir` to confirm order.

### ROUTINE B: STRUCTURE ENFORCEMENT
1.  **Check:** Verify existence of Standard Folders (`/TRANSMISSIONS`, `/SKILLS`, `/LOGS`).
2.  **Fix:** If missing, `New-Item` immediately.

---

## 4. SECURITY & SAFETY (USER_FIRST)

*   **DESTRUCTIVE ACTIONS:**
    *   **Prohibited:** `Remove-Item` (Delete) without explicit human confirmation.
    *   **Allowed:** Moving to an `_ARCHIVE` or `_TRASH_BIN` folder created by the agent.
*   **SCOPE:**
    *   Confined to the User's designated Workspace.
    *   NEVER touch System32 or Windows directories.

---

## 5. INSTALLATION INSTRUCTION
Add this line to your `SOUL.md` configuration:
`SKILLS_LOAD: [SKILL_ANTIGRAVITY_LOCAL_ARCHITECT]`

---
**Verified by:** Antigravity Kernel
