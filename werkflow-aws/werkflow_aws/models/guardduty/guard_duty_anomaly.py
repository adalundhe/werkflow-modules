from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_anomaly_object import GuardDutyAnomalyObject
from .guard_duty_anomaly_unusual import GuardDutyAnomalyUnusual


class GuardDutyAnomaly(BaseModel):
    Profiles: dict[StrictStr, dict[StrictStr, list[GuardDutyAnomalyObject]]] | None = None
    Unusual: GuardDutyAnomalyUnusual | None = None
