from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_agent_status import ConnectAgentStatus


class ConnectSearchAgentStatusesResponse(BaseModel):
    AgentStatuses: list[ConnectAgentStatus] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
