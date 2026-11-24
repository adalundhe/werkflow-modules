from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_agent_status_summary import ConnectAgentStatusSummary


class ConnectListAgentStatusesResponse(BaseModel):
    NextToken: StrictStr | None = None
    AgentStatusSummaryList: list[ConnectAgentStatusSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
