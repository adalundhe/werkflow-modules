from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerTrainingPlanExtension(BaseModel):
    TrainingPlanExtensionOfferingId: StrictStr | None = None
    ExtendedAt: datetime.datetime | StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    PaymentStatus: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    DurationHours: StrictInt | None = None
    UpfrontFee: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
