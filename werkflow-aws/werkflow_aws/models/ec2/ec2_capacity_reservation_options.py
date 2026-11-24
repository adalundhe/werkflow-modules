from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2CapacityReservationOptions(BaseModel):
    UsageStrategy: StrictStr | None = None
