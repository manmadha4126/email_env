from app.env import EmailEnv
from app.models import Action

env = EmailEnv()

print("[START]")

obs = env.reset()

for step in range(5):
    # Simple rule-based agent (no API)
    email = obs.inbox[step % len(obs.inbox)]

    if email.priority == "low":
        action = Action(type="delete", email_id=email.id)
    elif email.priority == "high":
        action = Action(type="reply", email_id=email.id)
    else:
        action = Action(type="classify", email_id=email.id)

    obs, reward, done, _ = env.step(action)

    print(f"[STEP] step={step} reward={reward}")

    if done:
        break

print("[END]")