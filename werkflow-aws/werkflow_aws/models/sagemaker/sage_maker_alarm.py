from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAlarm(BaseModel):
    AlarmName: StrictStr | None = None
