from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_coip_address_usage import EC2CoipAddressUsage


class EC2GetCoipPoolUsageResponse(BaseModel):
    CoipPoolId: StrictStr | None = None
    CoipAddressUsages: list[EC2CoipAddressUsage] | None = None
    LocalGatewayRouteTableId: StrictStr | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
