from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamQueryDimensionMapping(BaseModel):
    Name: StrictStr | None = None
    DimensionValueType: StrictStr | None = None
