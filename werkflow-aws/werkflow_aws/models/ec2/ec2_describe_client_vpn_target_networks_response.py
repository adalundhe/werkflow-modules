from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_target_network import EC2TargetNetwork


class EC2DescribeClientVpnTargetNetworksResponse(BaseModel):
    ClientVpnTargetNetworks: list[EC2TargetNetwork] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
