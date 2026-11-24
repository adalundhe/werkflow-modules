from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTScheduledJobRollout(BaseModel):
    startTime: StrictStr | None = None
