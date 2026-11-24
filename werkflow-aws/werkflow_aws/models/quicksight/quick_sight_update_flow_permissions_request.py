from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_permission import QuickSightPermission


class QuickSightUpdateFlowPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    FlowId: StrictStr
    GrantPermissions: list[QuickSightPermission] | None = None
    RevokePermissions: list[QuickSightPermission] | None = None
