from pydantic import BaseModel
from typing import List, Optional

class Email(BaseModel):
    id: int
    subject: str
    body: str
    priority: str

class Observation(BaseModel):
    inbox: List[Email]
    last_action: Optional[str]

class Action(BaseModel):
    type: str   # "classify", "reply", "delete"
    email_id: int
    content: Optional[str] = None

class Reward(BaseModel):
    score: float
    reason: str