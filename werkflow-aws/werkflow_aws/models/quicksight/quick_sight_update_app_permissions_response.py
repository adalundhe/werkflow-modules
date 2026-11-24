from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightUpdateAppPermissionsResponse(BaseModel):
    Arn: StrictStr | None = None
    AppId: StrictStr | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    Visibility: StrictStr | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
