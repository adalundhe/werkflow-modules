from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .el_bv2_ipam_pools import ELBv2IpamPools
from .el_bv2_subnet_mapping import ELBv2SubnetMapping
from .el_bv2_tag import ELBv2Tag


class ELBv2CreateLoadBalancerRequest(BaseModel):
    Name: StrictStr
    Subnets: list[StrictStr] | None = None
    SubnetMappings: list[ELBv2SubnetMapping] | None = None
    SecurityGroups: list[StrictStr] | None = None
    Scheme: Literal['internet-facing', 'internal'] | None = None
    Tags: list[ELBv2Tag] | None = None
    Type: Literal['application', 'network', 'gateway'] | None = None
    IpAddressType: Literal['ipv4', 'dualstack', 'dualstack-without-public-ipv4'] | None = None
    CustomerOwnedIpv4Pool: StrictStr | None = None
    EnablePrefixForIpv6SourceNat: Literal['on', 'off'] | None = None
    IpamPools: ELBv2IpamPools | None = None
