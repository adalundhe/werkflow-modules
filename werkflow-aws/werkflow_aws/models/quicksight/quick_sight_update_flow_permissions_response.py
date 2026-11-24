from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_permission import QuickSightPermission


class QuickSightUpdateFlowPermissionsResponse(BaseModel):
    Status: StrictInt | None = None
    Arn: StrictStr | None = None
    Permissions: list[QuickSightPermission] | None = None
    RequestId: StrictStr | None = None
    FlowId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
