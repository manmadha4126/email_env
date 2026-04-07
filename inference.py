import os
import json
from openai import OpenAI
from app.env import EmailEnv
from app.models import Action

# ✅ REQUIRED: Use hackathon environment variables
client = OpenAI(
    api_key=os.environ.get("API_KEY", "test_key"),
    base_url=os.environ.get("API_BASE_URL", "https://api.openai.com/v1")
)

MODEL = os.environ.get("MODEL_NAME", "gpt-4o-mini")

env = EmailEnv()

print("[START]")

obs = env.reset()

for step in range(5):
    # Convert observation to string
    prompt = f"""
You are an intelligent email assistant.

Inbox:
{obs}

Decide the best next action.

Available actions:
- classify (label: low/medium/high)
- reply (content required)
- delete
- escalate

Return ONLY valid JSON:
{{"type": "...", "email_id": ..., "label": "...", "content": "..."}}
"""

    # ✅ THIS CALL IS REQUIRED FOR VALIDATION
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content

    # ✅ Safe JSON parsing
    try:
        action_dict = json.loads(output)
    except:
        # fallback action (prevents crash)
        action_dict = {
            "type": "classify",
            "email_id": 1,
            "label": "medium"
        }

    # Convert to Action model
    try:
        action = Action(**action_dict)
    except:
        action = Action(type="classify", email_id=1, label="medium")

    # Step environment
    obs, reward, done, _ = env.step(action)

    print(f"[STEP] step={step} reward={reward}")

    if done:
        break

print("[END]")