from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_icmp_type_code import EC2IcmpTypeCode
from .ec2_port_range import EC2PortRange


class EC2ReplaceNetworkAclEntryRequest(BaseModel):
    NetworkAclId: StrictStr
    RuleNumber: StrictInt
    Protocol: StrictStr
    RuleAction: Literal['allow', 'deny']
    Egress: StrictBool
    DryRun: StrictBool | None = None
    CidrBlock: StrictStr | None = None
    Ipv6CidrBlock: StrictStr | None = None
    IcmpTypeCode: EC2IcmpTypeCode | None = None
    PortRange: EC2PortRange | None = None
