from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .iam_attached_permissions_boundary_model import IAMAttachedPermissionsBoundaryModel
from .iam_attached_policy_model import IAMAttachedPolicyModel
from .iam_instance_profile_model import IAMInstanceProfileModel
from .iam_policy_detail import IAMPolicyDetail
from .iam_role_last_used_model import IAMRoleLastUsedModel
from .iam_tag_model import IAMTagModel


class IAMRoleDetail(BaseModel):
    Path: StrictStr | None = None
    RoleName: StrictStr | None = None
    RoleId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    AssumeRolePolicyDocument: StrictStr | None = None
    InstanceProfileList: list[IAMInstanceProfileModel] | None = None
    RolePolicyList: list[IAMPolicyDetail] | None = None
    AttachedManagedPolicies: list[IAMAttachedPolicyModel] | None = None
    PermissionsBoundary: IAMAttachedPermissionsBoundaryModel | None = None
    Tags: list[IAMTagModel] | None = None
    RoleLastUsed: IAMRoleLastUsedModel | None = None
