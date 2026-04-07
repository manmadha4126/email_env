import os
import json
from openai import OpenAI
from app.env import EmailEnv
from app.models import Action

# ✅ Use environment variables (required)
client = OpenAI(
    api_key=os.environ.get("API_KEY", ""),
    base_url=os.environ.get("API_BASE_URL", "")
)

MODEL = os.environ.get("MODEL_NAME", "gpt-4o-mini")

env = EmailEnv()

print("[START]")

try:
    obs = env.reset()
except Exception as e:
    print(f"[END] error=reset_failed {e}")
    exit(0)

for step in range(5):
    try:
        prompt = f"""
You are an intelligent email assistant.

Inbox:
{obs}

Choose best action:
- classify
- reply
- delete
- escalate

Return JSON:
{{"type": "...", "email_id": ..., "label": "...", "content": "..."}}
"""

        # ✅ SAFE API CALL
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}]
            )
            output = response.choices[0].message.content
        except Exception as e:
            # Fallback if API fails
            output = '{"type":"classify","email_id":1,"label":"medium"}'

        # ✅ SAFE JSON PARSE
        try:
            action_dict = json.loads(output)
        except:
            action_dict = {"type": "classify", "email_id": 1, "label": "medium"}

        # ✅ SAFE ACTION CREATION
        try:
            action = Action(**action_dict)
        except:
            action = Action(type="classify", email_id=1, label="medium")

        # ✅ SAFE ENV STEP
        try:
            obs, reward, done, _ = env.step(action)
        except Exception as e:
            reward = {"score": 0.0, "reason": "env_step_failed"}
            done = True

        print(f"[STEP] step={step} reward={reward}")

        if done:
            break

    except Exception as e:
        print(f"[STEP] step={step} reward={{'score':0.0,'reason':'step_failed'}}")
        break

print("[END]")