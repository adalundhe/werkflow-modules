from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTGeoLocationTarget(BaseModel):
    name: StrictStr | None = None
    order: StrictStr | None = None
