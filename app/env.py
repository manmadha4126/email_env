import random
from app.models import Observation, Action, Reward, Email
from app.reward import compute_reward

class EmailEnv:
    def __init__(self):
        self.emails = []
        self.done = False
        self.steps = 0

    def reset(self):
        self.emails = [
            Email(id=1, subject="Meeting", body="Schedule meeting", priority="medium"),
            Email(id=2, subject="Urgent bug", body="System down!", priority="high"),
            Email(id=3, subject="Newsletter", body="Weekly news", priority="low"),
        ]
        self.done = False
        self.steps = 0

        return Observation(inbox=self.emails, last_action=None)

    def step(self, action: Action):
        self.steps += 1

        reward = compute_reward(action, self.emails)

        if self.steps > 5:
            self.done = True

        obs = Observation(inbox=self.emails, last_action=action.type)

        return obs, reward, self.done, {}

    def state(self):
        return {
            "emails": [e.dict() for e in self.emails],
            "steps": self.steps
        }