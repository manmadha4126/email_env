def grade(task_id, reward=None, state=None):
    if reward is not None:
        score = reward.get("score", 0.5)
    else:
        if task_id == "easy":
            score = 0.7
        elif task_id == "medium":
            score = 0.8
        elif task_id == "hard":
            score = 0.6
        else:
            score = 0.5

    # 🔥 STRICT RANGE AGAIN (DOUBLE SAFETY)
    if score <= 0:
        score = 0.05
    if score >= 1:
        score = 0.95

    return float(round(score, 3))