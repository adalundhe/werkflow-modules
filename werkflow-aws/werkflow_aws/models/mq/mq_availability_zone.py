from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MQAvailabilityZone(BaseModel):
    Name: StrictStr | None = None
