from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EC2CapacityBlockExtensionOffering(BaseModel):
    CapacityBlockExtensionOfferingId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    CapacityBlockExtensionStartDate: datetime.datetime | StrictStr | None = None
    CapacityBlockExtensionEndDate: datetime.datetime | StrictStr | None = None
    CapacityBlockExtensionDurationHours: StrictInt | None = None
    UpfrontFee: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
    Tenancy: StrictStr | None = None
    ZoneType: StrictStr | None = None
