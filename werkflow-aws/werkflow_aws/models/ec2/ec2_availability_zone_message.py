from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AvailabilityZoneMessage(BaseModel):
    Message: StrictStr | None = None
