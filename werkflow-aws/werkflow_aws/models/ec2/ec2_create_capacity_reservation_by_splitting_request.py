from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateCapacityReservationBySplittingRequest(BaseModel):
    SourceCapacityReservationId: StrictStr
    InstanceCount: StrictInt
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
