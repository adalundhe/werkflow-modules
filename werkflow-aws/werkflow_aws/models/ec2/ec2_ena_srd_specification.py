from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ec2_ena_srd_udp_specification import EC2EnaSrdUdpSpecification


class EC2EnaSrdSpecification(BaseModel):
    EnaSrdEnabled: StrictBool | None = None
    EnaSrdUdpSpecification: EC2EnaSrdUdpSpecification | None = None
