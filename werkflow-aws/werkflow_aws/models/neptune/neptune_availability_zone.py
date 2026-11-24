from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneAvailabilityZone(BaseModel):
    Name: StrictStr | None = None
