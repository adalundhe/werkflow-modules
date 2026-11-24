from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_transit_gateway_policy_table import EC2TransitGatewayPolicyTable


class EC2DescribeTransitGatewayPolicyTablesResponse(BaseModel):
    TransitGatewayPolicyTables: list[EC2TransitGatewayPolicyTable] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
