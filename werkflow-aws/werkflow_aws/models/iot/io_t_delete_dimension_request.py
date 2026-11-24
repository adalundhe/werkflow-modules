from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeleteDimensionRequest(BaseModel):
    name: StrictStr
