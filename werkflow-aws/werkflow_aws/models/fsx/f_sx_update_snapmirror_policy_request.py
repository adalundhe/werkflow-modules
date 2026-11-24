from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .f_sx_snapmirror_policy_retention_rule import FSxSnapmirrorPolicyRetentionRule


class FSxUpdateSnapmirrorPolicyRequest(BaseModel):
    SnapmirrorPolicyId: StrictStr
    ClientRequestToken: StrictStr | None = None
    RetentionRules: list[FSxSnapmirrorPolicyRetentionRule] | None = None
    TransferSchedule: StrictStr | None = None
    NetworkCompressionEnabled: StrictBool | None = None
    ThrottleInKbps: StrictInt | None = None
