from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ec2_attachment_ena_srd_udp_specification import EC2AttachmentEnaSrdUdpSpecification


class EC2AttachmentEnaSrdSpecification(BaseModel):
    EnaSrdEnabled: StrictBool | None = None
    EnaSrdUdpSpecification: EC2AttachmentEnaSrdUdpSpecification | None = None
