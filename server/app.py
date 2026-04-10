from fastapi import FastAPI
from app.env import EmailEnv

app = FastAPI()
env = EmailEnv()


@app.get("/")
def root():
    return {"status": "running"}


# MUST BE POST (VERY IMPORTANT)
@app.post("/reset")
def reset():
    obs = env.reset()
    return {
        "inbox": [e.dict() for e in obs.inbox],
        "last_action": obs.last_action
    }


@app.get("/state")
def state():
    return env.state()


@app.post("/step")
def step(action: dict):
    from app.models import Action

    action_obj = Action(**action)
    obs, reward, done, info = env.step(action_obj)

    return {
        "observation": {
            "inbox": [e.dict() for e in obs.inbox],
            "last_action": obs.last_action
        },
        "reward": reward,
        "done": done,
        "info": info
    }


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()