from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_dhcp_configuration import EC2DhcpConfiguration
from .ec2_tag_model import EC2TagModel


class EC2DhcpOptions(BaseModel):
    OwnerId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    DhcpOptionsId: StrictStr | None = None
    DhcpConfigurations: list[EC2DhcpConfiguration] | None = None
