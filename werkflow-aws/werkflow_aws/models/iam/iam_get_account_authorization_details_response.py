from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_group_detail import IAMGroupDetail
from .iam_managed_policy_detail import IAMManagedPolicyDetail
from .iam_role_detail import IAMRoleDetail
from .iam_user_detail import IAMUserDetail


class IAMGetAccountAuthorizationDetailsResponse(BaseModel):
    UserDetailList: list[IAMUserDetail] | None = None
    GroupDetailList: list[IAMGroupDetail] | None = None
    RoleDetailList: list[IAMRoleDetail] | None = None
    Policies: list[IAMManagedPolicyDetail] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
