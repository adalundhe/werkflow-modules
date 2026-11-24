from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateVpnGatewayRequest(BaseModel):
    Type: Literal['ipsec.1']
    AvailabilityZone: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    AmazonSideAsn: StrictInt | None = None
    DryRun: StrictBool | None = None
