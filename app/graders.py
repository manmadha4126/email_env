def grade(task_id, reward):
    score = reward.get("score", 0.5)

    # ensure strict range
    if score <= 0.0:
        score = 0.01
    elif score >= 1.0:
        score = 0.99

    return score

def grade_medium(state):
    return 0.8  # simplified


def grade_hard(state):
    return 0.6