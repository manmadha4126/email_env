from app.models import Action, Email


def compute_reward(action: Action, emails: list[Email]):
    score = 0.5  # SAFE starting point (never 0)
    reason = ""

    target_email = next((e for e in emails if e.id == action.email_id), None)

    if not target_email:
        return {"score": 0.1, "reason": "Invalid email"}

    # ------------------------
    # CLASSIFY
    # ------------------------
    if action.type == "classify":
        if action.label == target_email.priority:
            score += 0.25
            reason = "Correct classification"
        else:
            score -= 0.2
            reason = "Wrong classification"

    # ------------------------
    # REPLY
    # ------------------------
    elif action.type == "reply":
        content = (action.content or "").lower()

        if target_email.priority == "high":
            if "sorry" in content or "fix" in content:
                score += 0.3
                reason = "Good urgent reply"
            else:
                score += 0.15
                reason = "Weak reply"
        else:
            score -= 0.25
            reason = "Unnecessary reply"

    # ------------------------
    # DELETE
    # ------------------------
    elif action.type == "delete":
        if target_email.priority == "low":
            score += 0.3
            reason = "Correct delete"
        else:
            score -= 0.3
            reason = "Wrong delete"

    # ------------------------
    # ESCALATE
    # ------------------------
    elif action.type == "escalate":
        if target_email.priority == "high":
            score += 0.3
            reason = "Correct escalation"
        else:
            score -= 0.25
            reason = "Unnecessary escalation"

    # ------------------------
    # INVALID ACTION
    # ------------------------
    else:
        score -= 0.2
        reason = "Invalid action"

    # ------------------------
    # STEP PENALTY
    # ------------------------
    score -= 0.05

    # ------------------------
    # 🔥 STRICT RANGE ENFORCEMENT
    # ------------------------
    if score <= 0.0:
        score = 0.05
    elif score >= 1.0:
        score = 0.95

    return {
        "score": round(score, 3),  # extra safety
        "reason": reason
    }