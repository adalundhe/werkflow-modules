from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CapacityReservationGroup(BaseModel):
    GroupArn: StrictStr | None = None
    OwnerId: StrictStr | None = None
