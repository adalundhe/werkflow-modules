from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUpdateBrandAssignmentRequest(BaseModel):
    AwsAccountId: StrictStr
    BrandArn: StrictStr
