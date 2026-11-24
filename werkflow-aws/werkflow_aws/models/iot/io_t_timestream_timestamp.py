from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTTimestreamTimestamp(BaseModel):
    value: StrictStr | None = None
    unit: StrictStr | None = None
