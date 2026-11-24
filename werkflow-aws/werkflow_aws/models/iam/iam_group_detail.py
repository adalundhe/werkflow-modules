from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .iam_attached_policy_model import IAMAttachedPolicyModel
from .iam_policy_detail import IAMPolicyDetail


class IAMGroupDetail(BaseModel):
    Path: StrictStr | None = None
    GroupName: StrictStr | None = None
    GroupId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    GroupPolicyList: list[IAMPolicyDetail] | None = None
    AttachedManagedPolicies: list[IAMAttachedPolicyModel] | None = None
