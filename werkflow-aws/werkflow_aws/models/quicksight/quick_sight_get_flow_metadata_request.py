from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGetFlowMetadataRequest(BaseModel):
    AwsAccountId: StrictStr
    FlowId: StrictStr
