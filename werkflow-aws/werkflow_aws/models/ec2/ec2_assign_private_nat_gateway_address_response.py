from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_nat_gateway_address import EC2NatGatewayAddress


class EC2AssignPrivateNatGatewayAddressResponse(BaseModel):
    NatGatewayId: StrictStr | None = None
    NatGatewayAddresses: list[EC2NatGatewayAddress] | None = None
    ResponseMetadata: dict[str, Any] | None = None
