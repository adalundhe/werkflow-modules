from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteBrandAssignmentRequest(BaseModel):
    AwsAccountId: StrictStr
