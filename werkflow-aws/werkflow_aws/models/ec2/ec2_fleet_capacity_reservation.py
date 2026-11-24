from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class EC2FleetCapacityReservation(BaseModel):
    CapacityReservationId: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    InstancePlatform: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    TotalInstanceCount: StrictInt | None = None
    FulfilledCapacity: StrictFloat | StrictInt | None = None
    EbsOptimized: StrictBool | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    Weight: StrictFloat | StrictInt | None = None
    Priority: StrictInt | None = None
