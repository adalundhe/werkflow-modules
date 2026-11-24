from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .emr_on_demand_capacity_reservation_options import EMROnDemandCapacityReservationOptions


class EMROnDemandResizingSpecification(BaseModel):
    TimeoutDurationMinutes: StrictInt | None = None
    AllocationStrategy: StrictStr | None = None
    CapacityReservationOptions: EMROnDemandCapacityReservationOptions | None = None
