from fastapi import APIRouter
from typing import List

from .config import AGENTS
from .schemas import AgentInfo

router = APIRouter(prefix="/agents", tags=["agents"])

@router.get("/", response_model=List[AgentInfo])
async def get_agents() -> List[AgentInfo]:
    """
    Get list of available agents.
    
    Returns:
        List[AgentInfo]: List of agent information
    """
    agents_list = []
    for agent_id, agent_data in AGENTS.items():
        agent_info = AgentInfo(
            id=agent_id,
            name=agent_data["name"],
            description=agent_data["description"]
        )
        agents_list.append(agent_info)
    
    return agents_list