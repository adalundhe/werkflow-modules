from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_security_group import GuardDutySecurityGroup


class GuardDutyVpcConfig(BaseModel):
    SubnetIds: list[StrictStr] | None = None
    VpcId: StrictStr | None = None
    SecurityGroups: list[GuardDutySecurityGroup] | None = None
