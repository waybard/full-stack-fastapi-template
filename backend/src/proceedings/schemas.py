from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str
    agent_id: str


class SummaryResponse(BaseModel):
    summary: str
    agent_id: str