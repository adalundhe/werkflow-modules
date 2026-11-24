from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerTrainingPlanExtensionOffering(BaseModel):
    TrainingPlanExtensionOfferingId: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
    DurationHours: StrictInt | None = None
    UpfrontFee: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
