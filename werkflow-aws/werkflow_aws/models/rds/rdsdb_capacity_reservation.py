from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_available_capacity_per_availability_zone import RDSAvailableCapacityPerAvailabilityZone
from .rdsdb_capacity_reservation_commitment_info import RDSDBCapacityReservationCommitmentInfo
from .rds_tag_model import RDSTagModel


class RDSDBCapacityReservation(BaseModel):
    DBCapacityReservationName: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    Engine: StrictStr | None = None
    LicenseModel: StrictStr | None = None
    ReservedCapacityPerAvailabilityZone: StrictInt | None = None
    AvailableCapacityPerAvailabilityZoneList: list[RDSAvailableCapacityPerAvailabilityZone] | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    CommitmentInfo: RDSDBCapacityReservationCommitmentInfo | None = None
    State: StrictStr | None = None
    DBCapacityReservationArn: StrictStr | None = None
    DBCapacityReservationIdentifier: StrictStr | None = None
    TagList: list[RDSTagModel] | None = None
