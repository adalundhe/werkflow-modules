from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2CapacityBlock(BaseModel):
    CapacityBlockId: StrictStr | None = None
    UltraserverType: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    CapacityReservationIds: list[StrictStr] | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
