from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .athena_capacity_assignment import AthenaCapacityAssignment


class AthenaCapacityAssignmentConfiguration(BaseModel):
    CapacityReservationName: StrictStr | None = None
    CapacityAssignments: list[AthenaCapacityAssignment] | None = None
