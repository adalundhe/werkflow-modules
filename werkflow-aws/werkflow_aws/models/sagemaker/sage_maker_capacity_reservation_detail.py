from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerCapacityReservationDetail(BaseModel):
    SMCapacityReservationArn: StrictStr | None = None
    SMCapacityReservationId: StrictStr | None = None
    Owner: StrictStr | None = None
    Status: StrictStr | None = None
    InstanceType: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    TotalInstanceCount: StrictInt | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
