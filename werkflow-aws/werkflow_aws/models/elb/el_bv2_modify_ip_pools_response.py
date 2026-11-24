from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .el_bv2_ipam_pools import ELBv2IpamPools


class ELBv2ModifyIpPoolsResponse(BaseModel):
    IpamPools: ELBv2IpamPools | None = None
    ResponseMetadata: dict[str, Any] | None = None
