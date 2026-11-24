from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_icmp_type_code import EC2IcmpTypeCode
from .ec2_port_range import EC2PortRange


class EC2NetworkAclEntry(BaseModel):
    CidrBlock: StrictStr | None = None
    Egress: StrictBool | None = None
    IcmpTypeCode: EC2IcmpTypeCode | None = None
    Ipv6CidrBlock: StrictStr | None = None
    PortRange: EC2PortRange | None = None
    Protocol: StrictStr | None = None
    RuleAction: StrictStr | None = None
    RuleNumber: StrictInt | None = None
