from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncDeleteAgentRequest(BaseModel):
    AgentArn: StrictStr
