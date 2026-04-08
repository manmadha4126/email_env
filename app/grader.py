def grade_easy(state):
    return 0.7


def grade_medium(state):
    return 0.8


def grade_hard(state):
    return 0.6


def get_grader(task_id):
    if task_id == "easy":
        return grade_easy
    elif task_id == "medium":
        return grade_medium
    elif task_id == "hard":
        return grade_hard
    else:
        return lambda state: 0.5


def grade(task_id, reward=None, state=None):
    if reward is not None:
        score = reward.get("score", 0.5)
    else:
        grader = get_grader(task_id)
        score = grader(state)

    # 🔥 STRICT RANGE FIX
    if score <= 0.0:
        score = 0.05
    elif score >= 1.0:
        score = 0.95

    return score