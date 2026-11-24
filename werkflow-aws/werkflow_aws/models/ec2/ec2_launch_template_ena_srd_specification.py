from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ec2_launch_template_ena_srd_udp_specification import EC2LaunchTemplateEnaSrdUdpSpecification


class EC2LaunchTemplateEnaSrdSpecification(BaseModel):
    EnaSrdEnabled: StrictBool | None = None
    EnaSrdUdpSpecification: EC2LaunchTemplateEnaSrdUdpSpecification | None = None
