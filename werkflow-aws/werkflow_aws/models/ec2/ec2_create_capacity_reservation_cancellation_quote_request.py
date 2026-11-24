from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateCapacityReservationCancellationQuoteRequest(BaseModel):
    CapacityReservationId: StrictStr
    ClientToken: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
