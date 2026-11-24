from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .connect_agent_status import ConnectAgentStatus


class ConnectDescribeAgentStatusResponse(BaseModel):
    AgentStatus: ConnectAgentStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
