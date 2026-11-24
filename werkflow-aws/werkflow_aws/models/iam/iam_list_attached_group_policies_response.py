from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_attached_policy_model import IAMAttachedPolicyModel


class IAMListAttachedGroupPoliciesResponse(BaseModel):
    AttachedPolicies: list[IAMAttachedPolicyModel] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
