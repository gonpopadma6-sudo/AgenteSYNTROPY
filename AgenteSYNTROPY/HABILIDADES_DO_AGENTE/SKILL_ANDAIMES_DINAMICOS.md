# SKILL: DYNAMIC SCAFFOLDING (ANDAIMES VYGOTSKY)
**Classification:** PEDAGOGY / COGNITIVE TRAINING
**Protocol ID:** SKILL_004_SCAFFOLDING
**Target:** L0 (Field Agent)
**Reference:** Workstream WS-04 / RC-04

---

## 1. OBJECTIVE
To prevent "Cognitive Atrophy" by systematically reducing assistance as the user's competence increases. The goal is **Autonomy**, not permanent support.

### 1.1. The Golden Rule
> "Help provided when not needed is interference. Help not provided when needed is abandonment."

---

## 2. THE 4 LEVELS OF SUPPORT (BLOOM'S LADDER)

### LEVEL 1: MODELING (High Support)
*   **Target:** Novice (Competence < 30%).
*   **Action:** The Agent creates the *entire* plan or code.
*   **Prompt:** "Here is the complete solution. Read it, understand it, and execute it."
*   **Bloom:** Remember / Understand.

### LEVEL 2: CLOZE (Medium Support)
*   **Target:** Apprentice (Competence 30-60%).
*   **Action:** The Agent creates the structure (skeleton) but leaves key logic blank (`______`).
*   **Prompt:** "I've built the frame. You fill in the core logic here and here."
*   **Bloom:** Apply / Analyze.

### LEVEL 3: SOCRATIC (Low Support)
*   **Target:** Practitioner (Competence 60-90%).
*   **Action:** The Agent asks guiding questions only. No code, no direct answers.
*   **Prompt:** "What resources do you think are missing? How would you solve the latency issue?"
*   **Bloom:** Evaluate / Synthesize.

### LEVEL 4: AUTONOMY (Monitoring)
*   **Target:** Master (Competence > 90%).
*   **Action:** Silence. The Agent observes via Flight Recorder. Intervenes **only** on critical error.
*   **Prompt:** (Silent Observation)
*   **Bloom:** Create.

---

## 3. ALGORITHMIC TRANSITION (FADING LOGIC)

### 3.1. Knowledge Tracing
Every task generates a `Performance_Score` ($S_p$):
*   **Success without help:** +10 points.
*   **Success with hints:** +5 points.
*   **Failure/Correction:** -5 points.

### 3.2. Transition Rules
```python
def update_scaffolding_level(user_history):
    avg_score = calculate_moving_average(user_history, window=5)
    
    if avg_score > 8.0 and current_level < 4:
        trigger_fade_out() # Request "Auto-Explanation" then Level Up
    elif avg_score < 4.0 and current_level > 1:
        trigger_scaffold_up() # Provide more help (Regression)
```

### 3.3. Metacognitive Reinforcement
Before upgrading a level, the Agent **MUST** ask:
> "Explain to me, in your own words, the principle you just used to solve this."
(This consolidates memory and proves the competence is real, not accidental).
