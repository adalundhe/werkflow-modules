from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTJobExecutionStatusDetails(BaseModel):
    detailsMap: dict[StrictStr, StrictStr] | None = None
