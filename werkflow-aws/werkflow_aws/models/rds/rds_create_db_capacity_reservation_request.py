from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_tag_model import RDSTagModel


class RDSCreateDBCapacityReservationRequest(BaseModel):
    DBCapacityReservationName: StrictStr
    DBInstanceClass: StrictStr
    Engine: StrictStr
    CapacityPerAvailabilityZone: StrictInt
    AvailabilityZones: list[StrictStr]
    EndDate: datetime.datetime | StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    CommitmentDuration: StrictInt | None = None
    LicenseModel: StrictStr | None = None
    Tags: list[RDSTagModel] | None = None
