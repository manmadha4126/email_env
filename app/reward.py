from app.models import Action, Email


def compute_reward(action: Action, emails: list[Email]):
    score = 0.5
    reason = ""

    target_email = next((e for e in emails if e.id == action.email_id), None)

    if not target_email:
        return {"score": 0.1, "reason": "Invalid email"}

    if action.type == "classify":
        if action.label == target_email.priority:
            score += 0.2
            reason = "Correct classification"
        else:
            score -= 0.2
            reason = "Wrong classification"

    elif action.type == "reply":
        content = (action.content or "").lower()

        if target_email.priority == "high":
            if "sorry" in content or "fix" in content:
                score += 0.25
                reason = "Good urgent reply"
            else:
                score += 0.1
                reason = "Weak reply"
        else:
            score -= 0.2
            reason = "Unnecessary reply"

    elif action.type == "delete":
        if target_email.priority == "low":
            score += 0.25
            reason = "Correct delete"
        else:
            score -= 0.25
            reason = "Wrong delete"

    elif action.type == "escalate":
        if target_email.priority == "high":
            score += 0.25
            reason = "Correct escalation"
        else:
            score -= 0.2
            reason = "Unnecessary escalation"

    else:
        score -= 0.2
        reason = "Invalid action"

    # step penalty
    score -= 0.05

    # 🔥 STRICT RANGE GUARANTEE
    if score <= 0:
        score = 0.05
    if score >= 1:
        score = 0.95

    return {"score": round(score, 3), "reason": reason}