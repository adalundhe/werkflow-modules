from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sts_policy_descriptor_type import STSPolicyDescriptorType


class STSAssumeRoleWithSAMLRequest(BaseModel):
    RoleArn: StrictStr
    PrincipalArn: StrictStr
    SAMLAssertion: StrictStr
    PolicyArns: list[STSPolicyDescriptorType] | None = None
    Policy: StrictStr | None = None
    DurationSeconds: StrictInt | None = None
    MinimumSessionTokenSize: StrictInt | None = None
