from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .el_bv2_load_balancer_address import ELBv2LoadBalancerAddress


class ELBv2AvailabilityZone(BaseModel):
    ZoneName: StrictStr | None = None
    SubnetId: StrictStr | None = None
    OutpostId: StrictStr | None = None
    LoadBalancerAddresses: list[ELBv2LoadBalancerAddress] | None = None
    SourceNatIpv6Prefixes: list[StrictStr] | None = None
