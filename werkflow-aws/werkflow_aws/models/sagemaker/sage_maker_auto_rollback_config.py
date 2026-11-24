from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_alarm import SageMakerAlarm


class SageMakerAutoRollbackConfig(BaseModel):
    Alarms: list[SageMakerAlarm] | None = None
