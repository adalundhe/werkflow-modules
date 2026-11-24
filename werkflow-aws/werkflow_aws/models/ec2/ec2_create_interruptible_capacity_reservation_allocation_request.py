from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateInterruptibleCapacityReservationAllocationRequest(BaseModel):
    CapacityReservationId: StrictStr
    InstanceCount: StrictInt
    ClientToken: StrictStr | None = None
    DryRun: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    ZeroSizePreference: Literal['retain', 'default'] | None = None
