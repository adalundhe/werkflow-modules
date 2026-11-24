from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_outpost_lag import EC2OutpostLag


class EC2DescribeOutpostLagsResponse(BaseModel):
    OutpostLags: list[EC2OutpostLag] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
