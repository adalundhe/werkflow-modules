from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_filter_port_range import EC2FilterPortRange


class EC2PathFilter(BaseModel):
    SourceAddress: StrictStr | None = None
    SourcePortRange: EC2FilterPortRange | None = None
    DestinationAddress: StrictStr | None = None
    DestinationPortRange: EC2FilterPortRange | None = None
