from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeBrandAssignmentRequest(BaseModel):
    AwsAccountId: StrictStr
