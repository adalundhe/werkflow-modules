from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_agent_summary import QuickSightAgentSummary


class QuickSightSearchAgentsResponse(BaseModel):
    AgentSummaries: list[QuickSightAgentSummary] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
