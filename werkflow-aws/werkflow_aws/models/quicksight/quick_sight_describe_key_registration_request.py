from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightDescribeKeyRegistrationRequest(BaseModel):
    AwsAccountId: StrictStr
    DefaultKeyOnly: StrictBool | None = None
