from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayAvailabilityZoneDetail(BaseModel):
    Name: StrictStr | None = None
