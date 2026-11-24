from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AvailabilityZoneSubGeography(BaseModel):
    Name: StrictStr | None = None
