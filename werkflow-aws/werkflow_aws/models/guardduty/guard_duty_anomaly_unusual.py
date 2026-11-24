from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_anomaly_object import GuardDutyAnomalyObject


class GuardDutyAnomalyUnusual(BaseModel):
    Behavior: dict[StrictStr, dict[StrictStr, GuardDutyAnomalyObject]] | None = None
