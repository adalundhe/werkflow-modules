from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ec2_ena_srd_udp_specification_request import EC2EnaSrdUdpSpecificationRequest


class EC2EnaSrdSpecificationRequest(BaseModel):
    EnaSrdEnabled: StrictBool | None = None
    EnaSrdUdpSpecification: EC2EnaSrdUdpSpecificationRequest | None = None
