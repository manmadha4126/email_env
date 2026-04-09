from app.models import Action, Email


def compute_reward(action: Action, emails: list[Email]):
    score = 0.5
    reason = ""

    target_email = next((e for e in emails if e.id == action.email_id), None)

    if not target_email:
        return {"score": 0.1, "reason": "Invalid email"}

    if action.type == "classify":
        score += 0.2 if action.label == target_email.priority else -0.2
        reason = "Classification"

    elif action.type == "reply":
        content = (action.content or "").lower()
        if target_email.priority == "high":
            score += 0.25 if ("sorry" in content or "fix" in content) else 0.1
        else:
            score -= 0.2
        reason = "Reply"

    elif action.type == "delete":
        score += 0.25 if target_email.priority == "low" else -0.25
        reason = "Delete"

    elif action.type == "escalate":
        score += 0.25 if target_email.priority == "high" else -0.2
        reason = "Escalate"

    else:
        score -= 0.2
        reason = "Invalid"

    score -= 0.05

    # 🔥 STRICT RANGE (FINAL)
    if score <= 0.0:
        score = 0.05
    elif score >= 1.0:
        score = 0.95

    return {"score": float(round(score, 3)), "reason": reason}