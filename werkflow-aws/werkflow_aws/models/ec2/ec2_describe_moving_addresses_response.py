from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_moving_address_status import EC2MovingAddressStatus


class EC2DescribeMovingAddressesResponse(BaseModel):
    MovingAddressStatuses: list[EC2MovingAddressStatus] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
