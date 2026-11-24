from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightDescribeAppPermissionsResponse(BaseModel):
    AppId: StrictStr | None = None
    Arn: StrictStr | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
