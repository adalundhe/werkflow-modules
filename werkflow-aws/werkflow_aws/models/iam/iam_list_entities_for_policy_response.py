from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_policy_group import IAMPolicyGroup
from .iam_policy_role import IAMPolicyRole
from .iam_policy_user import IAMPolicyUser


class IAMListEntitiesForPolicyResponse(BaseModel):
    PolicyGroups: list[IAMPolicyGroup] | None = None
    PolicyUsers: list[IAMPolicyUser] | None = None
    PolicyRoles: list[IAMPolicyRole] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
