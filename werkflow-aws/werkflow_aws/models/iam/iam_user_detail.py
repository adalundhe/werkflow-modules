from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .iam_attached_permissions_boundary_model import IAMAttachedPermissionsBoundaryModel
from .iam_attached_policy_model import IAMAttachedPolicyModel
from .iam_policy_detail import IAMPolicyDetail
from .iam_tag_model import IAMTagModel


class IAMUserDetail(BaseModel):
    Path: StrictStr | None = None
    UserName: StrictStr | None = None
    UserId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    UserPolicyList: list[IAMPolicyDetail] | None = None
    GroupList: list[StrictStr] | None = None
    AttachedManagedPolicies: list[IAMAttachedPolicyModel] | None = None
    PermissionsBoundary: IAMAttachedPermissionsBoundaryModel | None = None
    Tags: list[IAMTagModel] | None = None
