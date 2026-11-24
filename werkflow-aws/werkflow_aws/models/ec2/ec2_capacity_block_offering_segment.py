from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EC2CapacityBlockOfferingSegment(BaseModel):
    InstanceType: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    CapacityBlockDurationHours: StrictInt | None = None
    CapacityBlockDurationMinutes: StrictInt | None = None
    UpfrontFee: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
    ZoneType: StrictStr | None = None
