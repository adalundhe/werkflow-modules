from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_metering_policy_entry import EC2TransitGatewayMeteringPolicyEntry


class EC2GetTransitGatewayMeteringPolicyEntriesResponse(BaseModel):
    TransitGatewayMeteringPolicyEntries: list[EC2TransitGatewayMeteringPolicyEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
