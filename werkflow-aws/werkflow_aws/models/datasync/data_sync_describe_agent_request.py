from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncDescribeAgentRequest(BaseModel):
    AgentArn: StrictStr
