from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightUpdateSelfUpgradeRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr
    UpgradeRequestId: StrictStr
    Action: Literal['APPROVE', 'DENY', 'VERIFY']
