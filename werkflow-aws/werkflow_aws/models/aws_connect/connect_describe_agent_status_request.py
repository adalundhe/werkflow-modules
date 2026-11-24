from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeAgentStatusRequest(BaseModel):
    InstanceId: StrictStr
    AgentStatusId: StrictStr
