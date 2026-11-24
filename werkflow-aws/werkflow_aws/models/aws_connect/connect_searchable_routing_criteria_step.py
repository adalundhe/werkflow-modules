from __future__ import annotations
from pydantic import BaseModel
from .connect_searchable_agent_criteria_step import ConnectSearchableAgentCriteriaStep


class ConnectSearchableRoutingCriteriaStep(BaseModel):
    AgentCriteria: ConnectSearchableAgentCriteriaStep | None = None
