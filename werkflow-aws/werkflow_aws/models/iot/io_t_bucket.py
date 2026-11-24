from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTBucket(BaseModel):
    keyValue: StrictStr | None = None
    count: StrictInt | None = None
