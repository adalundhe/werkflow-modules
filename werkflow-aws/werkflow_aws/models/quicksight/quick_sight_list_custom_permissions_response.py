from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_custom_permissions import QuickSightCustomPermissions


class QuickSightListCustomPermissionsResponse(BaseModel):
    Status: StrictInt | None = None
    CustomPermissionsList: list[QuickSightCustomPermissions] | None = None
    NextToken: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
