from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerReservedCapacitySummary(BaseModel):
    ReservedCapacityArn: StrictStr | None = None
    ReservedCapacityType: StrictStr | None = None
    UltraServerType: StrictStr | None = None
    UltraServerCount: StrictInt | None = None
    InstanceType: StrictStr | None = None
    TotalInstanceCount: StrictInt | None = None
    Status: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    DurationHours: StrictInt | None = None
    DurationMinutes: StrictInt | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
