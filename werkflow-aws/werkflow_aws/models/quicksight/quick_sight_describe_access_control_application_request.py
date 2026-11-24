from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAccessControlApplicationRequest(BaseModel):
    AwsAccountId: StrictStr
    ApplicationId: StrictStr
