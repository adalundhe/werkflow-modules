from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .athena_capacity_assignment import AthenaCapacityAssignment


class AthenaPutCapacityAssignmentConfigurationRequest(BaseModel):
    CapacityReservationName: StrictStr
    CapacityAssignments: list[AthenaCapacityAssignment]
