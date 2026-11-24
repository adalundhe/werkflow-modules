from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_link_sharing_configuration import QuickSightLinkSharingConfiguration
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightUpdateDashboardPermissionsResponse(BaseModel):
    DashboardArn: StrictStr | None = None
    DashboardId: StrictStr | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    LinkSharingConfiguration: QuickSightLinkSharingConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
