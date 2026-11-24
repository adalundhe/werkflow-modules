from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2GetGroupsForCapacityReservationRequest(BaseModel):
    CapacityReservationId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    DryRun: StrictBool | None = None
