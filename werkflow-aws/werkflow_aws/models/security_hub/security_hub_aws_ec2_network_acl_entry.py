from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .security_hub_icmp_type_code import SecurityHubIcmpTypeCode
from .security_hub_port_range_from_to import SecurityHubPortRangeFromTo


class SecurityHubAwsEc2NetworkAclEntry(BaseModel):
    CidrBlock: StrictStr | None = None
    Egress: StrictBool | None = None
    IcmpTypeCode: SecurityHubIcmpTypeCode | None = None
    Ipv6CidrBlock: StrictStr | None = None
    PortRange: SecurityHubPortRangeFromTo | None = None
    Protocol: StrictStr | None = None
    RuleAction: StrictStr | None = None
    RuleNumber: StrictInt | None = None
