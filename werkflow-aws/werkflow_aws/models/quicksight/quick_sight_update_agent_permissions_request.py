from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightUpdateAgentPermissionsRequest(BaseModel):
    AgentId: StrictStr
    AwsAccountId: StrictStr
    GrantPermissions: list[QuickSightResourcePermission] | None = None
    RevokePermissions: list[QuickSightResourcePermission] | None = None
