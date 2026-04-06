from app.models import Action, Email

def compute_reward(action: Action, emails: list[Email]):
    score = 0.0
    reason = ""

    # Find target email
    target_email = next((e for e in emails if e.id == action.email_id), None)

    if not target_email:
        return {"score": 0.0, "reason": "Invalid email ID"}

    # ------------------------
    # CLASSIFY
    # ------------------------
    if action.type == "classify":
        if action.label == target_email.priority:
            score += 0.5
            reason = "Correct classification"
        else:
            score -= 0.3
            reason = "Wrong classification"

    # ------------------------
    # REPLY
    # ------------------------
    elif action.type == "reply":
        content = action.content or ""

        if target_email.priority == "high":
            if "sorry" in content.lower() or "fix" in content.lower():
                score += 1.0
                reason = "Good urgent response with empathy"
            else:
                score += 0.6
                reason = "Replied but lacks proper tone"
        else:
            score -= 0.4
            reason = "Unnecessary reply"

    # ------------------------
    # DELETE
    # ------------------------
    elif action.type == "delete":
        if target_email.priority == "low":
            score += 1.0
            reason = "Correct deletion of low priority email"
        else:
            score -= 0.8
            reason = "Deleted important email"

    # ------------------------
    # ESCALATE (ADVANCED)
    # ------------------------
    elif action.type == "escalate":
        if target_email.priority == "high":
            score += 1.0
            reason = "Correct escalation"
        else:
            score -= 0.5
            reason = "Unnecessary escalation"

    # ------------------------
    # INVALID ACTION
    # ------------------------
    else:
        score -= 0.5
        reason = "Invalid action type"

    # ------------------------
    # STEP PENALTY (efficiency)
    # ------------------------
    score -= 0.05

    # ------------------------
    # CLAMP SCORE (0 → 1)
    # ------------------------
    score = max(0.0, min(1.0, score))

    return {
        "score": score,
        "reason": reason
    }