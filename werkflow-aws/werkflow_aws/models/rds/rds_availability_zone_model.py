from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSAvailabilityZoneModel(BaseModel):
    Name: StrictStr | None = None
