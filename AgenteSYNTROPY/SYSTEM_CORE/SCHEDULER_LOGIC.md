# SYSTEM LOGIC: SCHEDULER_MEMORIA_DISTRIBUIDA

**ID:** LOGIC_001_SPACED_REPETITION
**Target Node:** L1 (Orchestrator)
**Algorithm:** Modified Fibonacci/Exponential Backoff (Protocol "2357")

---

## 1. THE "2357" PROTOCOL
To maximize retention and combat the Forgetting Curve, review sessions must be scheduled at specific intervals after the **First Exposure (Day 0)**.

| Intervention | Interval | Target Retention | Mechanism |
| :--- | :--- | :--- | :--- |
| **Review 1** | **+2 Days** | 60% -> 90% | Stabilization |
| **Review 2** | **+5 Days** | 70% -> 90% | Consolidation |
| **Review 3** | **+10 Days** | 80% -> 95% | Integration |
| **Review 4** | **+17 Days** | 85% -> 99% | Crystallization |

## 2. SCHEDULING ALGORITHM

### Input
*   `Topic_ID`: Unique identifier of the concept (e.g., "Python_Lists").
*   `Date_Last_Seen`: Timestamp.
*   `Performance_Score`: 0 (Fail) to 5 (Perfect Recall).

### Calculation Logic (Pseudo-Code)
```python
def calculate_next_review(topic, last_review_date, performance):
    intervals = [2, 5, 10, 17]
    current_stage = topic.stage_index # 0, 1, 2, 3
    
    if performance < 3:
        # Regression: Reset to Stage 0 or 1
        return current_date + timedelta(days=1)
    
    if current_stage < len(intervals):
        next_interval = intervals[current_stage]
        return last_review_date + timedelta(days=next_interval)
    else:
        # Graduation: Log to Permanent Wisdom
        return None 
```

## 3. INTERFACE WITH HOST
*   **Daily Check:** At session start, L1 checks `MEMORY_SCHEDULE.md` (to be created/maintained in logs).
*   **Prompt:** "Hoje temos {N} tópicos para o protocolo de recuperação: [Topic A, Topic B]. Vamos começar?"

---

**HASH:** [SCHEDULER_LOGIC_V1_2026]
