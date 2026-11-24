from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_policy_parameter import IAMPolicyParameter


class IAMDelegationPermission(BaseModel):
    PolicyTemplateArn: StrictStr | None = None
    Parameters: list[IAMPolicyParameter] | None = None
