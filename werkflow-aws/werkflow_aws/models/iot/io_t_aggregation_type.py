from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAggregationType(BaseModel):
    name: StrictStr | None = None
    values: list[StrictStr] | None = None
