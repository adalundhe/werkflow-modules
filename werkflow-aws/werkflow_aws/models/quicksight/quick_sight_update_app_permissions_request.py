from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightUpdateAppPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    AppId: StrictStr
    GrantPermissions: list[QuickSightResourcePermission] | None = None
    RevokePermissions: list[QuickSightResourcePermission] | None = None
    Visibility: Literal['PRIVATE', 'PUBLIC'] | None = None
