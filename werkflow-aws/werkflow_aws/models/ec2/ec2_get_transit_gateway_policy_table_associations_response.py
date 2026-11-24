from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_policy_table_association import EC2TransitGatewayPolicyTableAssociation


class EC2GetTransitGatewayPolicyTableAssociationsResponse(BaseModel):
    Associations: list[EC2TransitGatewayPolicyTableAssociation] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
