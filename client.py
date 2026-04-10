from app.env import EmailEnv
from app.models import Action


class Client:
    def __init__(self):
        self.env = EmailEnv()

    def reset(self):
        return self.env.reset()

    def step(self, action_dict):
        action = Action(**action_dict)
        obs, reward, done, info = self.env.step(action)

        return {
            "observation": obs.dict(),
            "reward": reward.dict(),
            "done": done,
            "info": info
        }

    def state(self):
        return self.env.state()