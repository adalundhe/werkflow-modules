from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_carrier_gateway import EC2CarrierGateway


class EC2DeleteCarrierGatewayResponse(BaseModel):
    CarrierGateway: EC2CarrierGateway | None = None
    ResponseMetadata: dict[str, Any] | None = None
