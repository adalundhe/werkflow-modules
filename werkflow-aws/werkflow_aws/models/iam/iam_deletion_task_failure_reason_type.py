from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_role_usage_type import IAMRoleUsageType


class IAMDeletionTaskFailureReasonType(BaseModel):
    Reason: StrictStr | None = None
    RoleUsageList: list[IAMRoleUsageType] | None = None
