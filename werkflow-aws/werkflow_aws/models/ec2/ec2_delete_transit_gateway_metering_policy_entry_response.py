from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_transit_gateway_metering_policy_entry import EC2TransitGatewayMeteringPolicyEntry


class EC2DeleteTransitGatewayMeteringPolicyEntryResponse(BaseModel):
    TransitGatewayMeteringPolicyEntry: EC2TransitGatewayMeteringPolicyEntry | None = None
    ResponseMetadata: dict[str, Any] | None = None
