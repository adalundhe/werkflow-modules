from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .guard_duty_scan_threat_name import GuardDutyScanThreatName


class GuardDutyThreatDetectedByName(BaseModel):
    ItemCount: StrictInt | None = None
    UniqueThreatNameCount: StrictInt | None = None
    Shortened: StrictBool | None = None
    ThreatNames: list[GuardDutyScanThreatName] | None = None
