from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerReservedCapacityOffering(BaseModel):
    ReservedCapacityType: StrictStr | None = None
    UltraServerType: StrictStr | None = None
    UltraServerCount: StrictInt | None = None
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    DurationHours: StrictInt | None = None
    DurationMinutes: StrictInt | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ExtensionStartTime: datetime.datetime | StrictStr | None = None
    ExtensionEndTime: datetime.datetime | StrictStr | None = None
