from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAssetPropertyTimestamp(BaseModel):
    timeInSeconds: StrictStr | None = None
    offsetInNanos: StrictStr | None = None
