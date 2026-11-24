from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_ultra_server_summary import SageMakerUltraServerSummary


class SageMakerDescribeReservedCapacityResponse(BaseModel):
    ReservedCapacityArn: StrictStr | None = None
    ReservedCapacityType: StrictStr | None = None
    Status: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    DurationHours: StrictInt | None = None
    DurationMinutes: StrictInt | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    InstanceType: StrictStr | None = None
    TotalInstanceCount: StrictInt | None = None
    AvailableInstanceCount: StrictInt | None = None
    InUseInstanceCount: StrictInt | None = None
    UltraServerSummary: SageMakerUltraServerSummary | None = None
    ResponseMetadata: dict[str, Any] | None = None
