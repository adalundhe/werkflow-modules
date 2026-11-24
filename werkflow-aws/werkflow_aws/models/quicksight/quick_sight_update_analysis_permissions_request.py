from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_resource_permission import QuickSightResourcePermission


class QuickSightUpdateAnalysisPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    AnalysisId: StrictStr
    GrantPermissions: list[QuickSightResourcePermission] | None = None
    RevokePermissions: list[QuickSightResourcePermission] | None = None
