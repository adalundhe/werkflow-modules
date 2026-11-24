from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_port_range import EC2PortRange


class EC2AnalysisSecurityGroupRule(BaseModel):
    Cidr: StrictStr | None = None
    Direction: StrictStr | None = None
    SecurityGroupId: StrictStr | None = None
    PortRange: EC2PortRange | None = None
    PrefixListId: StrictStr | None = None
    Protocol: StrictStr | None = None
