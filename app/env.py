from app.models import Observation, Action, Email
from app.reward import compute_reward
from app.tasks import get_tasks


class EmailEnv:
    def __init__(self):
        self.emails = []
        self.done = False
        self.steps = 0

    def reset(self):
        self.emails = [
            Email(id=1, subject="Team Meeting", body="Schedule a meeting tomorrow", priority="medium"),
            Email(id=2, subject="URGENT: Server Down", body="Production system is down!", priority="high"),
            Email(id=3, subject="Newsletter", body="Weekly updates", priority="low"),
            Email(id=4, subject="Client Complaint", body="Customer is unhappy", priority="high"),
            Email(id=5, subject="Promo Offer", body="50% discount", priority="low"),
        ]

        self.done = False
        self.steps = 0

        return Observation(inbox=self.emails, last_action=None)

    def step(self, action: Action):
        self.steps += 1

        reward = compute_reward(action, self.emails)

        if self.steps >= 5:
            self.done = True

        obs = Observation(inbox=self.emails, last_action=action.type)

        # 🔥 TASK MAPPING (IMPORTANT)
        task = "easy"
        if action.type == "reply":
            task = "medium"
        elif action.type in ["escalate", "delete"]:
            task = "hard"

        return obs, reward, self.done, {"task": task}

    def state(self):
        return {
            "emails": [e.dict() for e in self.emails],
            "steps": self.steps
        }

    # 🔥 REQUIRED BY VALIDATOR
    def tasks(self):
        return get_tasks()