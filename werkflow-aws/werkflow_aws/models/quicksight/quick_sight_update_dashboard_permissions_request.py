from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightUpdateDashboardPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardId: StrictStr
    GrantPermissions: list[QuickSightResourcePermission] | None = None
    RevokePermissions: list[QuickSightResourcePermission] | None = None
    GrantLinkPermissions: list[QuickSightResourcePermission] | None = None
    RevokeLinkPermissions: list[QuickSightResourcePermission] | None = None
