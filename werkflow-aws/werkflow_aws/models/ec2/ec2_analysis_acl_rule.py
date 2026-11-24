from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_port_range import EC2PortRange


class EC2AnalysisAclRule(BaseModel):
    Cidr: StrictStr | None = None
    Egress: StrictBool | None = None
    PortRange: EC2PortRange | None = None
    Protocol: StrictStr | None = None
    RuleAction: StrictStr | None = None
    RuleNumber: StrictInt | None = None
