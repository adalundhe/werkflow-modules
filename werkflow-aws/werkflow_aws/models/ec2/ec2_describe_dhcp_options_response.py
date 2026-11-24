from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_dhcp_options import EC2DhcpOptions


class EC2DescribeDhcpOptionsResponse(BaseModel):
    NextToken: StrictStr | None = None
    DhcpOptions: list[EC2DhcpOptions] | None = None
    ResponseMetadata: dict[str, Any] | None = None
