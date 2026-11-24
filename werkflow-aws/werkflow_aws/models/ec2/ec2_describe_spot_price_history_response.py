from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_spot_price import EC2SpotPrice


class EC2DescribeSpotPriceHistoryResponse(BaseModel):
    NextToken: StrictStr | None = None
    SpotPriceHistory: list[EC2SpotPrice] | None = None
    ResponseMetadata: dict[str, Any] | None = None
