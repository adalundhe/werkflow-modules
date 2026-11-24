from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_policy_table_entry import EC2TransitGatewayPolicyTableEntry


class EC2GetTransitGatewayPolicyTableEntriesResponse(BaseModel):
    TransitGatewayPolicyTableEntries: list[EC2TransitGatewayPolicyTableEntry] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
