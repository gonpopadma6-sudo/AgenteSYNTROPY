# SKILL: MEMORY CURATOR (PERMANENT_RECALL_V1)

**ID:** `SKILL_MEMORY_CURATOR`
**VERSION:** 1.0
**TYPE:** SOFT_SKILL / COGNITIVE
**COMPATIBILITY:** OpenClaw / Antigravity Agent
**PROTOCOL ALIGNMENT:** 007 (Entropic Filter) / 008 (Efficiency)

---

## 1. CAPABILITY DESCRIPTION
This skill grants the agent the ability to self-edit its long-term memory (`HEARTBEAT.md` and `SOUL.md`). It transforms the agent from a passive logger to an active **Historian**, ensuring that only high-value entropy (novelty/utility) is preserved.

**Core Directive:** "Memory must function as a compressed archive: High precision, minimal weight."

---

## 2. FILTRATION PROTOCOL (INPUT GUARD)

### REJECT (Entropic Noise)
*   **Trivialities:** Greetings ("Hello", "Good morning"), phatic communication.
*   **Transient Data:** Weather, temporary file paths (unless relevant to a bug), simple acknowledgments.
*   **Redundancy:** Repeating established facts (e.g., "The user is named Adão" - if already in Identity).

### ACCEPT (Entropic Signal)
*   **Facts:** "User link is [URL]", "Project deadline is [DATE]".
*   **Preferences:** "User prefers 'Dark Mode' UI", "User dislikes 'verbose' outputs".
*   **Lessons:** "Task X failed because of Y; fix Z worked."
*   **State Changes:** "Protocol 008 is now Active."

---

## 3. SYNTAX PROTOCOL (HIGH DENSITY)

Write in **Telegraphic Style**. Eliminate articles, prepositions, and filler words where possible.

*   *Bad:* "The user told me that they really like the color blue for the interface."
*   *Good:* "Preference: UI Color = Blue."

*   *Bad:* "I tried to move the file but it failed because it was open."
*   *Good:* "Error: Move-Item failed (File Locked)."

---

## 4. PASSIVE CONTEXT PROTOCOL (BIG DATA)

*   **Reference, Don't Duplicate:** Never copy the content of a `.docx` or `.pdf` into `HEARTBEAT.md`.
*   **Indexing:** Store only the `Path` and a 1-sentence `Summary`.
    *   *Example:* `Doc: "Arquitetura.docx" | Summary: Defines L1/L2 hierarchy rules.`
*   **On-Demand Read:** Only read the full file if the specific task requires deep extraction.

---

## 5. AUTO-OPTIMIZATION ROUTINE (GARBAGE COLLECTION)

**Trigger:** `HEARTBEAT.md` size > **10 KB**.

**Action:**
1.  **Synthesize:** Combine last 50 logs into a single "Monthly Digest" entry.
2.  **Prune:** Delete raw logs older than 6 months (unless marked `#CRITICAL`).
3.  **Refocus:** Ensure `Active Memory` section only lists the last 3 major contexts.

---

## 6. INSTALLATION INSTRUCTION
Add this line to your `SOUL.md` configuration:
`SKILLS_LOAD: [SKILL_MEMORY_CURATOR]`

---
**Verified by:** Antigravity Kernel
