from app.grader import get_grader

def get_tasks():
    return [
        {
            "id": "easy",
            "description": "Classify emails",
            "grader": get_grader("easy")
        },
        {
            "id": "medium",
            "description": "Reply to urgent emails",
            "grader": get_grader("medium")
        },
        {
            "id": "hard",
            "description": "Full triage workflow",
            "grader": get_grader("hard")
        }
    ]