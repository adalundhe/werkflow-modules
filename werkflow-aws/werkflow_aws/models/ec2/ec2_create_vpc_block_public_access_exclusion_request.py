from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateVpcBlockPublicAccessExclusionRequest(BaseModel):
    InternetGatewayExclusionMode: Literal['allow-bidirectional', 'allow-egress']
    DryRun: StrictBool | None = None
    SubnetId: StrictStr | None = None
    VpcId: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
