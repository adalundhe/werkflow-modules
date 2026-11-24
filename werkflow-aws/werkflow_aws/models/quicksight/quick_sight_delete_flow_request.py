from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteFlowRequest(BaseModel):
    AwsAccountId: StrictStr
    FlowId: StrictStr
