from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sts_policy_descriptor_type import STSPolicyDescriptorType


class STSAssumeRootRequest(BaseModel):
    TargetPrincipal: StrictStr
    TaskPolicyArn: STSPolicyDescriptorType
    DurationSeconds: StrictInt | None = None
    MinimumSessionTokenSize: StrictInt | None = None
