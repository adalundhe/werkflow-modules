from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_capacity_block_offering_segment import EC2CapacityBlockOfferingSegment


class EC2CapacityBlockOffering(BaseModel):
    CapacityBlockOfferingId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    CapacityBlockDurationHours: StrictInt | None = None
    UpfrontFee: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
    Tenancy: StrictStr | None = None
    UltraserverType: StrictStr | None = None
    UltraserverCount: StrictInt | None = None
    CapacityBlockDurationMinutes: StrictInt | None = None
    ZoneType: StrictStr | None = None
    CapacityBlockOfferingSegments: list[EC2CapacityBlockOfferingSegment] | None = None
