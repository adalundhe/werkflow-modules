from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_observations import GuardDutyObservations


class GuardDutyAnomalyObject(BaseModel):
    ProfileType: StrictStr | None = None
    ProfileSubtype: StrictStr | None = None
    Observations: GuardDutyObservations | None = None
