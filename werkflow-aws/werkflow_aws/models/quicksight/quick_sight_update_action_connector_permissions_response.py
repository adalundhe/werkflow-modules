from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightUpdateActionConnectorPermissionsResponse(BaseModel):
    Arn: StrictStr | None = None
    ActionConnectorId: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    ResponseMetadata: dict[str, Any] | None = None
