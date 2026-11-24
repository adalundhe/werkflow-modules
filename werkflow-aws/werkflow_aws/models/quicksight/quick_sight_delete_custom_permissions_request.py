from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteCustomPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    CustomPermissionsName: StrictStr
