from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTUpdateDimensionRequest(BaseModel):
    name: StrictStr
    stringValues: list[StrictStr]
