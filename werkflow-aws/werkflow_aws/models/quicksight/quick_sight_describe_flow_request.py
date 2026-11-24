from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightDescribeFlowRequest(BaseModel):
    AwsAccountId: StrictStr
    FlowId: StrictStr
    PublishState: Literal['PUBLISHED', 'DRAFT', 'PENDING_APPROVAL']
