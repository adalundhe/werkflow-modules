from __future__ import annotations
from pydantic import BaseModel
from .connect_agents_criteria import ConnectAgentsCriteria


class ConnectMatchCriteria(BaseModel):
    AgentsCriteria: ConnectAgentsCriteria | None = None
