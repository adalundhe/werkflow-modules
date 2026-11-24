from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAlarmModel(BaseModel):
    AlarmName: StrictStr | None = None
