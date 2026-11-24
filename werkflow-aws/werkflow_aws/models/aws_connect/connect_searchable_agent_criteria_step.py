from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ConnectSearchableAgentCriteriaStep(BaseModel):
    AgentIds: list[StrictStr] | None = None
    MatchType: Literal['MATCH_ALL', 'MATCH_ANY', 'MATCH_EXACT', 'MATCH_NONE'] | None = None
