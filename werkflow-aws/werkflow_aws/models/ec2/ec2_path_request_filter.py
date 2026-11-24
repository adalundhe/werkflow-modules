from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_request_filter_port_range import EC2RequestFilterPortRange


class EC2PathRequestFilter(BaseModel):
    SourceAddress: StrictStr | None = None
    SourcePortRange: EC2RequestFilterPortRange | None = None
    DestinationAddress: StrictStr | None = None
    DestinationPortRange: EC2RequestFilterPortRange | None = None
