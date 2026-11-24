from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateCapacityReservationDateChangeQuoteRequest(BaseModel):
    CapacityReservationId: StrictStr
    NewStartDate: datetime.datetime | StrictStr
    ClientToken: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
