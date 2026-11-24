from __future__ import annotations
from pydantic import BaseModel
from .connect_ai_agent_search_criteria import ConnectAiAgentSearchCriteria


class ConnectAiAgentsCriteria(BaseModel):
    Criteria: list[ConnectAiAgentSearchCriteria] | None = None
