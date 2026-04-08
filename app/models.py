from pydantic import BaseModel
from typing import List, Optional


class Email(BaseModel):
    id: int
    subject: str
    body: str
    priority: str


class Action(BaseModel):
    type: str
    email_id: int
    label: Optional[str] = None
    content: Optional[str] = None


class Observation(BaseModel):
    inbox: List[Email]
    last_action: Optional[str]


class Reward(BaseModel):
    score: float
    reason: str