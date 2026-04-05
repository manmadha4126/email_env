def grade_easy(state):
    deleted_low = True
    for e in state["emails"]:
        if e["priority"] == "low":
            deleted_low = False
    return 1.0 if deleted_low else 0.5


def grade_medium(state):
    return 0.8  # simplified


def grade_hard(state):
    return 0.6