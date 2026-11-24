from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .fms_security_group_rule_description import FMSSecurityGroupRuleDescription


class FMSSecurityGroupRemediationAction(BaseModel):
    RemediationActionType: StrictStr | None = None
    Description: StrictStr | None = None
    RemediationResult: FMSSecurityGroupRuleDescription | None = None
    IsDefaultAction: StrictBool | None = None
