from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaGetCapacityAssignmentConfigurationRequest(BaseModel):
    CapacityReservationName: StrictStr
