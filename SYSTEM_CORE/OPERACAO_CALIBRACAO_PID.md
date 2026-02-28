# OPERATIONAL PROTOCOL: PID CALIBRATION (BLACK BOX)
**Status:** ACTIVE
**Start Date:** 2026-02-18
**End Date:** 2026-02-25
**Target:** HEARTBEAT.md (Closed-Loop Stabilizer)

---

## 1. OBJECTIVE
Calibrate the coefficients $K_p, K_i, K_d$ of the emotional regulation controller to minimalize "Over-Correction" (System Anxiety) and "Under-Correction" (User Abandonment).

## 2. INITIAL PARAMETERS (T0)
*   **Proportional ($K_p$):** `0.5` (Moderate reactivity).
*   **Integral ($K_i$):** `0.1` (Slow accumulation of history).
*   **Derivative ($K_d$):** `0.2` (Dampening of sudden spikes).

## 3. MONITORING METRICS (VIA FLIGHT RECORDER)
The following metrics must be analyzed daily:

### 3.1. Overshoot Rate
*   **Definition:** Frequency where Agent intervention causes User Frustration to *increase*.
*   **Threshold:** > 5% implies $K_p$ is too high.

### 3.2. Settling Time
*   **Definition:** Time elapsed between `User_Error` and `User_Flow_State`.
*   **Target:** < 5 minutes.
*   **Adjustment:** If slower, increase $K_i$.

### 3.3. Steady-State Error
*   **Definition:** Persistent low-level friction (e.g., user re-reading text 3x).
*   **Adjustment:** If detected, check $K_d$ (Dampening might be too strong).

### 3.4. Loss Aversion Threshold (Aversão à Trama/Perda)
*   **Definition:** Medo endêmico de obsolescência tecnológica detectado na sintaxe do usuário (resistência andragógica).
*   **Adjustment:** Reduzir $K_p$ temporariamente e acionar as heurísticas de *Verbalização Empática* de `SKILL_ACTIVE_LISTENING_PID.md`.

---

## 4. DAILY LOG TEMPLATE
All anomalies must be appended to `LOGS/CALIBRATION_V2.log`:

```log
[DATE] [K_VALUES] [EVENT] [OUTCOME]
2026-02-18 | 0.5/0.1/0.2 | User stuck on 'Loop' | Agent hinted immediately (Too fast?) | Result: User ignored hint.
```

---

## 5. EXIT CRITERIA
*   **Success:** 7 consecutive days with `Settling Time` < 5min and `Overshoot Rate` < 2%.
*   **Failure:** `User_churn` (Abandonment) detected. -> **EMERGENCY ROLLBACK TO V1.**
