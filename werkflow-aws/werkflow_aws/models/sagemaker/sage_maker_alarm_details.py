from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAlarmDetails(BaseModel):
    AlarmName: StrictStr | None = None
