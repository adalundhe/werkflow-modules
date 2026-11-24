from __future__ import annotations
from pydantic import BaseModel
from .guard_duty_anomaly import GuardDutyAnomaly
from .guard_duty_sequence import GuardDutySequence


class GuardDutyDetection(BaseModel):
    Anomaly: GuardDutyAnomaly | None = None
    Sequence: GuardDutySequence | None = None
