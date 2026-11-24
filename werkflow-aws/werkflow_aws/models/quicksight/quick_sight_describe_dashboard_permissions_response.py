from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_link_sharing_configuration import QuickSightLinkSharingConfiguration
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightDescribeDashboardPermissionsResponse(BaseModel):
    DashboardId: StrictStr | None = None
    DashboardArn: StrictStr | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    Status: StrictInt | None = None
    RequestId: StrictStr | None = None
    LinkSharingConfiguration: QuickSightLinkSharingConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
