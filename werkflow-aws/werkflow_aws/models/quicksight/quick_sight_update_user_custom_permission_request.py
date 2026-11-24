from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUpdateUserCustomPermissionRequest(BaseModel):
    UserName: StrictStr
    AwsAccountId: StrictStr
    Namespace: StrictStr
    CustomPermissionsName: StrictStr
