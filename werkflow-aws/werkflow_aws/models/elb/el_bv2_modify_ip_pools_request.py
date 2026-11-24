from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .el_bv2_ipam_pools import ELBv2IpamPools


class ELBv2ModifyIpPoolsRequest(BaseModel):
    LoadBalancerArn: StrictStr
    IpamPools: ELBv2IpamPools | None = None
    RemoveIpamPools: list[Literal['ipv4']] | None = None
