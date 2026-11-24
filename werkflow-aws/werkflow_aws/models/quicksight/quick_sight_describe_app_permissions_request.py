from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAppPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    AppId: StrictStr
