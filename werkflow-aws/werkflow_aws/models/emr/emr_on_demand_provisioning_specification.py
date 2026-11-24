from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .emr_on_demand_capacity_reservation_options import EMROnDemandCapacityReservationOptions


class EMROnDemandProvisioningSpecification(BaseModel):
    AllocationStrategy: StrictStr | None = None
    CapacityReservationOptions: EMROnDemandCapacityReservationOptions | None = None
