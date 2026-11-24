from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_port_range import EC2PortRange


class EC2AnalysisPacketHeader(BaseModel):
    DestinationAddresses: list[StrictStr] | None = None
    DestinationPortRanges: list[EC2PortRange] | None = None
    Protocol: StrictStr | None = None
    SourceAddresses: list[StrictStr] | None = None
    SourcePortRanges: list[EC2PortRange] | None = None
