from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_nat_gateway import EC2NatGateway


class EC2CreateNatGatewayResponse(BaseModel):
    ClientToken: StrictStr | None = None
    NatGateway: EC2NatGateway | None = None
    ResponseMetadata: dict[str, Any] | None = None
