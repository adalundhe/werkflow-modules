from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightDescribeAgentPermissionsResponse(BaseModel):
    Arn: StrictStr | None = None
    AgentId: StrictStr | None = None
    Permissions: list[QuickSightResourcePermission] | None = None
    RequestId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
