from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .fms_network_acl_icmp_type_code import FMSNetworkAclIcmpTypeCode
from .fms_network_acl_port_range import FMSNetworkAclPortRange


class FMSNetworkAclEntry(BaseModel):
    IcmpTypeCode: FMSNetworkAclIcmpTypeCode | None = None
    Protocol: StrictStr | None = None
    PortRange: FMSNetworkAclPortRange | None = None
    CidrBlock: StrictStr | None = None
    Ipv6CidrBlock: StrictStr | None = None
    RuleAction: StrictStr | None = None
    Egress: StrictBool | None = None
