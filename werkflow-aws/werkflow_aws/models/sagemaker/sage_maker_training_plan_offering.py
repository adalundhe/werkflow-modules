from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_reserved_capacity_offering import SageMakerReservedCapacityOffering


class SageMakerTrainingPlanOffering(BaseModel):
    TrainingPlanOfferingId: StrictStr | None = None
    TargetResources: list[StrictStr] | None = None
    RequestedStartTimeAfter: datetime.datetime | StrictStr | None = None
    RequestedEndTimeBefore: datetime.datetime | StrictStr | None = None
    DurationHours: StrictInt | None = None
    DurationMinutes: StrictInt | None = None
    UpfrontFee: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
    ReservedCapacityOfferings: list[SageMakerReservedCapacityOffering] | None = None
