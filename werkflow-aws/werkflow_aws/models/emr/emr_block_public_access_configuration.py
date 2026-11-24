from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .emr_port_range import EMRPortRange


class EMRBlockPublicAccessConfiguration(BaseModel):
    BlockPublicSecurityGroupRules: StrictBool | None = None
    PermittedPublicSecurityGroupRuleRanges: list[EMRPortRange] | None = None
