from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightGetFlowPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    FlowId: StrictStr
