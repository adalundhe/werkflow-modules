from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .el_bv2_capacity_reservation_status import ELBv2CapacityReservationStatus


class ELBv2ZonalCapacityReservationState(BaseModel):
    State: ELBv2CapacityReservationStatus | None = None
    AvailabilityZone: StrictStr | None = None
    EffectiveCapacityUnits: StrictFloat | StrictInt | None = None
