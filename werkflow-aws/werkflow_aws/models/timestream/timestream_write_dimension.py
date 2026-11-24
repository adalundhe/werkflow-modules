from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class TimestreamWriteDimension(BaseModel):
    Name: StrictStr
    Value: StrictStr
    DimensionValueType: Literal['VARCHAR'] | None = None
