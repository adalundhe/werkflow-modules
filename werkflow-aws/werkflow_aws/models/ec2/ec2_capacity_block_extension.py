from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EC2CapacityBlockExtension(BaseModel):
    CapacityReservationId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    CapacityBlockExtensionOfferingId: StrictStr | None = None
    CapacityBlockExtensionDurationHours: StrictInt | None = None
    CapacityBlockExtensionStatus: StrictStr | None = None
    CapacityBlockExtensionPurchaseDate: datetime.datetime | StrictStr | None = None
    CapacityBlockExtensionStartDate: datetime.datetime | StrictStr | None = None
    CapacityBlockExtensionEndDate: datetime.datetime | StrictStr | None = None
    UpfrontFee: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
    ZoneType: StrictStr | None = None
