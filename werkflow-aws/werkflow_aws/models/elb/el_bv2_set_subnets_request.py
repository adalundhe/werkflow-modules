from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .el_bv2_subnet_mapping import ELBv2SubnetMapping


class ELBv2SetSubnetsRequest(BaseModel):
    LoadBalancerArn: StrictStr
    Subnets: list[StrictStr] | None = None
    SubnetMappings: list[ELBv2SubnetMapping] | None = None
    IpAddressType: Literal['ipv4', 'dualstack', 'dualstack-without-public-ipv4'] | None = None
    EnablePrefixForIpv6SourceNat: Literal['on', 'off'] | None = None
