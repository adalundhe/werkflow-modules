from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_partial_match import FMSPartialMatch
from .fms_security_group_remediation_action import FMSSecurityGroupRemediationAction


class FMSAwsVPCSecurityGroupViolation(BaseModel):
    ViolationTarget: StrictStr | None = None
    ViolationTargetDescription: StrictStr | None = None
    PartialMatches: list[FMSPartialMatch] | None = None
    PossibleSecurityGroupRemediationActions: list[FMSSecurityGroupRemediationAction] | None = None
