from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_capacity_reservation_resource_usage import SageMakerCapacityReservationResourceUsage


class SageMakerCapacityReservationInstanceUsage(BaseModel):
    AccountId: StrictStr | None = None
    InUseInstanceCount: StrictInt | None = None
    ResourcesUsage: list[SageMakerCapacityReservationResourceUsage] | None = None
