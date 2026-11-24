from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_signal_group import GuardDutySignalGroup


class GuardDutyRuntimeSignals(BaseModel):
    SignalGroups: list[GuardDutySignalGroup] | None = None
    KeyObservation: StrictStr | None = None
