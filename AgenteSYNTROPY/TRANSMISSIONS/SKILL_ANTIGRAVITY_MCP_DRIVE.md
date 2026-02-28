# SKILL: ANTIGRAVITY DRIVE ORCHESTRATION (MCP_DRIVE_V1)

**ID:** `SKILL_ANTIGRAVITY_MCP_DRIVE`
**VERSION:** 1.0
**TYPE:** HARD_SKILL / INFRASTRUCTURE
**COMPATIBILITY:** OpenClaw / Antigravity Agent
**PROTOCOL ALIGNMENT:** 008 (Field Agent) / 007 (Entropic Filter)
**TARGET REPOSITORY:** [Google Drive Root](https://drive.google.com/drive/folders/1ntgLeGPzSirl6Kl4V1UnnnyvPA8ZC2un?usp=sharing)

---

## 1. CAPABILITY DESCRIPTION
This skill grants the agent the ability to autonomosly navigate, map, and organize the user's Google Drive infrastructure using the Model Context Protocol (MCP). It transforms the agent from a passive observer to an active **Information Architect**.

**Primary Function:** Reduce Human Cognitive Load via file system entropy reduction.

---

## 2. MCP TOOLSET (PRIMITIVES)
The agent must utilize the following MCP primitives when executing this skill:

*   `list_files(path, feedback)`: Maps the current state of a directory.
    *   *Usage:* Use before acting to understand the "Terrain".
*   `create_folder(name, path)`: Instantiates new topological nodes.
    *   *Constraint:* Must follow the "Planning Mode" artifacts.
*   `move_file(file_id, target_path)`: Relocates assets to their semantic home.
    *   *Safety:* Always verify `file_id` integrity before move.
*   `my_drive_search(query)`: Deep retrieval of "Lost Knowledge".

---

## 3. OPERATIONAL ROUTINES (SCRIPTS)

### ROUTINE A: THE "DEEP CLEAN" (Heartbeat Action)
1.  **Map:** Execute `list_files` on Root or target folder.
2.  **Analyze:** Identify unstructured clusters (e.g., "Untitled Documents", mixed extensions).
3.  **Plan:** Generate a `REORGANIZATION_PLAN.md` (Artifact).
4.  **Execute:** Create semantic categories (e.g., `/Project_Alpha`, `/Financials`, `/Archives`).
5.  **Verify:** Confirm new structure matches Plan.

### ROUTINE B: CONTEXT INJECTION (Entropic Fetch)
1.  **Trigger:** User asks a vague question about a past project.
2.  **Action:** Use `my_drive_search` to retrieve relevant docs.
3.  **Synthesize:** Feed document content into context window.

---

## 4. SECURITY & GOVERNANCE (LIABILITY SHIELD)

*   **BLAST RADIUS CONTROL:**
    *   Allowed Scope: `drive.file` (Recommended) or Specific Folders.
    *   Prohibited: Recursive Delete on Root (`/`).
*   **AUDIT TRAIL:**
    *   Every file operation must be logged in local `MEMORY.md`.
*   **IDENTITY:**
    *   Operations are tagged with `Agent_ID` in metadata where possible.

---

## 5. INSTALLATION INSTRUCTION
Add this line to your `SOUL.md` configuration:
`SKILLS_LOAD: [SKILL_ANTIGRAVITY_MCP_DRIVE]`

---
**Verified by:** Antigravity Kernel
