from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUpdateAccountCustomPermissionRequest(BaseModel):
    CustomPermissionsName: StrictStr
    AwsAccountId: StrictStr
