---
title: Email Triage Environment
emoji: 📧
colorFrom: blue
colorTo: green
sdk: docker
app_file: app.py
pinned: false
---

# Email Triage OpenEnv Environment

## Description
This environment simulates real-world email triage tasks where an AI agent must classify, respond, and manage emails efficiently.

## Tasks
1. Easy: Classify emails (low/medium/high)
2. Medium: Respond to urgent emails
3. Hard: Delete irrelevant or low-priority emails

## Action Space
- classify
- reply
- delete

## Observation Space
- Inbox emails (id, subject, body, priority)
- Last action taken

## Reward Function
- Correct classification → +0.7
- Correct urgent reply → +1.0
- Correct deletion → +1.0
- Incorrect action → penalty

## Endpoints
- /reset → resets environment
- /state → returns current state

## Setup
```bash
docker build -t email-env .
docker run email-env