from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_private_ip_address_details import GuardDutyPrivateIpAddressDetails
from .guard_duty_security_group import GuardDutySecurityGroup


class GuardDutyEc2NetworkInterface(BaseModel):
    Ipv6Addresses: list[StrictStr] | None = None
    PrivateIpAddresses: list[GuardDutyPrivateIpAddressDetails] | None = None
    PublicIp: StrictStr | None = None
    SecurityGroups: list[GuardDutySecurityGroup] | None = None
    SubNetId: StrictStr | None = None
    VpcId: StrictStr | None = None
