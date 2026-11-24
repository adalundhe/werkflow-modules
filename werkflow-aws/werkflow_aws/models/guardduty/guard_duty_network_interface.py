from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_private_ip_address_details import GuardDutyPrivateIpAddressDetails
from .guard_duty_security_group import GuardDutySecurityGroup


class GuardDutyNetworkInterface(BaseModel):
    Ipv6Addresses: list[StrictStr] | None = None
    NetworkInterfaceId: StrictStr | None = None
    PrivateDnsName: StrictStr | None = None
    PrivateIpAddress: StrictStr | None = None
    PrivateIpAddresses: list[GuardDutyPrivateIpAddressDetails] | None = None
    PublicDnsName: StrictStr | None = None
    PublicIp: StrictStr | None = None
    SecurityGroups: list[GuardDutySecurityGroup] | None = None
    SubnetId: StrictStr | None = None
    VpcId: StrictStr | None = None
