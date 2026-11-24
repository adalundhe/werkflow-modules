from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sts_policy_descriptor_type import STSPolicyDescriptorType
from .sts_tag import STSTag


class STSGetFederationTokenRequest(BaseModel):
    Name: StrictStr
    Policy: StrictStr | None = None
    PolicyArns: list[STSPolicyDescriptorType] | None = None
    DurationSeconds: StrictInt | None = None
    Tags: list[STSTag] | None = None
    MinimumSessionTokenSize: StrictInt | None = None
