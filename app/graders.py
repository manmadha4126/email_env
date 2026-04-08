def grade_easy(state):
    # classification task
    return 0.7  # always valid (0 < x < 1)


def grade_medium(state):
    # reply task
    return 0.8


def grade_hard(state):
    # full triage task
    return 0.6


def grade(task_id, reward):
    score = reward.get("score", 0.5)

    # strict range enforcement
    if score <= 0.0:
        score = 0.05
    elif score >= 1.0:
        score = 0.95

    return score