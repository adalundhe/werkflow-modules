from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateInternetGatewayRequest(BaseModel):
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
