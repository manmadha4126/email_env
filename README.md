---
title: Email Triage AI Environment
emoji: 📧
colorFrom: blue
colorTo: purple
sdk: docker
app_file: app.py
pinned: false
---

# 📧 Email Triage OpenEnv Environment

## 🚀 Overview
This project simulates a **real-world email triage system**, where AI agents must intelligently manage incoming emails.

It reflects real industry workflows in:
- Customer Support
- DevOps Alert Handling
- Business Communication Systems

---

## 🎯 Objective
Train and evaluate AI agents to:
- Classify email priority
- Respond appropriately
- Delete irrelevant emails
- Escalate critical issues

---

## 🧠 Tasks

### 🟢 Easy
Classify emails into:
- low / medium / high

### 🟡 Medium
Respond to urgent emails with proper tone

### 🔴 Hard
Multi-step reasoning:
- Detect urgency
- Respond correctly
- Escalate when required

---

## ⚙️ Action Space
- classify
- reply
- delete
- escalate

---

## 👀 Observation Space
- Email inbox (id, subject, body, priority)
- Last action taken

---

## 🏆 Reward Design

| Action | Reward |
|------|--------|
| Correct classification | +0.5 |
| Good urgent reply | +1.0 |
| Correct deletion | +1.0 |
| Correct escalation | +1.0 |
| Wrong action | penalty |
| Extra steps | -0.05 |

👉 Encourages:
- Accuracy
- Efficiency
- Human-like reasoning

---

## 🔌 API Endpoints

- POST `/reset`
- POST `/step`
- GET `/state`

---

## 🧪 Example Use Cases

- AI email assistants
- Customer support automation
- Incident response systems

---

## ⚡ Setup

```bash
docker build -t email-env .
docker run email-env