from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeDimensionRequest(BaseModel):
    name: StrictStr
