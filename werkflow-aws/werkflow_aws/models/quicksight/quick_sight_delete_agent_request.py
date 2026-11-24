from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteAgentRequest(BaseModel):
    AgentId: StrictStr
    AwsAccountId: StrictStr
