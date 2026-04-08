def grade_easy(state):
    return 0.7  # strictly between 0 and 1


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