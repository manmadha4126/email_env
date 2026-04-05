from app.models import Reward

def compute_reward(action, emails):
    score = 0.0
    reason = "No action matched"

    for e in emails:
        if e.id == action.email_id:

            if action.type == "classify":
                if e.priority == "high":
                    score = 1.0
                    reason = "Correct high priority classification"
                elif e.priority == "medium":
                    score = 0.7
                    reason = "Correct medium classification"
                else:
                    score = 0.5
                    reason = "Low priority classification"

            elif action.type == "delete":
                if e.priority == "low":
                    score = 1.0
                    reason = "Correct deletion of low priority email"
                else:
                    score = 0.0
                    reason = "Wrong deletion (important email removed)"

            elif action.type == "reply":
                if e.priority == "high":
                    score = 1.0
                    reason = "Correct reply to urgent email"
                elif e.priority == "medium":
                    score = 0.5
                    reason = "Unnecessary reply to medium email"
                else:
                    score = 0.2
                    reason = "Wrong reply to low priority email"

    return Reward(score=score, reason=reason)