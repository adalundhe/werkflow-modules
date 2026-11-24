from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightUpdateSpacePermissionsResponse(BaseModel):
    spaceId: StrictStr | None = None
    spaceArn: StrictStr | None = None
    permissions: list[QuickSightResourcePermission] | None = None
    requestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
