from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_capacity_reservation_instance_usage import SageMakerCapacityReservationInstanceUsage


class SageMakerGetCapacityReservationUsageResponse(BaseModel):
    SMCapacityReservationId: StrictStr | None = None
    TotalInstanceCount: StrictInt | None = None
    AvailableInstanceCount: StrictInt | None = None
    LastRefreshTime: datetime.datetime | StrictStr | None = None
    InstanceUsageSet: list[SageMakerCapacityReservationInstanceUsage] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
