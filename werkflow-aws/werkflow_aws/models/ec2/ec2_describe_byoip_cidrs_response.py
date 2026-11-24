from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_byoip_cidr import EC2ByoipCidr


class EC2DescribeByoipCidrsResponse(BaseModel):
    ByoipCidrs: list[EC2ByoipCidr] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
