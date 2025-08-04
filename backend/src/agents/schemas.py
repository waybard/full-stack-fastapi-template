from pydantic import BaseModel
from typing import Optional

class AgentInfo(BaseModel):
    id: str
    name: str
    description: Optional[str] = None