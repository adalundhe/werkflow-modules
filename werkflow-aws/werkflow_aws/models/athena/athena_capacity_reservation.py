from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .athena_capacity_allocation import AthenaCapacityAllocation


class AthenaCapacityReservation(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    TargetDpus: StrictInt | None = None
    AllocatedDpus: StrictInt | None = None
    LastAllocation: AthenaCapacityAllocation | None = None
    LastSuccessfulAllocationTime: datetime.datetime | StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
