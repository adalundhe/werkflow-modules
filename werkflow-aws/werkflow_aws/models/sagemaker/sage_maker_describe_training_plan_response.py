from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_reserved_capacity_summary import SageMakerReservedCapacitySummary


class SageMakerDescribeTrainingPlanResponse(BaseModel):
    TrainingPlanArn: StrictStr | None = None
    TrainingPlanName: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    DurationHours: StrictInt | None = None
    DurationMinutes: StrictInt | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    UpfrontFee: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
    TotalInstanceCount: StrictInt | None = None
    AvailableInstanceCount: StrictInt | None = None
    InUseInstanceCount: StrictInt | None = None
    UnhealthyInstanceCount: StrictInt | None = None
    AvailableSpareInstanceCount: StrictInt | None = None
    TotalUltraServerCount: StrictInt | None = None
    TargetResources: list[StrictStr] | None = None
    ReservedCapacitySummaries: list[SageMakerReservedCapacitySummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
