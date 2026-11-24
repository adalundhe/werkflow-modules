from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .guard_duty_total import GuardDutyTotal


class GuardDutyUsageFeatureResult(BaseModel):
    Feature: StrictStr | None = None
    Total: GuardDutyTotal | None = None
