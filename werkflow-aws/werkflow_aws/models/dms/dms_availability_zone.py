from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSAvailabilityZone(BaseModel):
    Name: StrictStr | None = None
