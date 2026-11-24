from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ec2_new_dhcp_configuration import EC2NewDhcpConfiguration
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateDhcpOptionsRequest(BaseModel):
    DhcpConfigurations: list[EC2NewDhcpConfiguration]
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
