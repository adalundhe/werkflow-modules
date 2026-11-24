from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZonePutResourceConfiguration(BaseModel):
    name: StrictStr
    region: StrictStr
    parameters: dict[StrictStr, StrictStr]
    description: StrictStr | None = None
