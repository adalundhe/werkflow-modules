from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateSubnetCidrReservationRequest(BaseModel):
    SubnetId: StrictStr
    Cidr: StrictStr
    ReservationType: Literal['prefix', 'explicit']
    Description: StrictStr | None = None
    DryRun: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
