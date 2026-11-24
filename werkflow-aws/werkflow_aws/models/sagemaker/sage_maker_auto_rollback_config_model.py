from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_alarm_model import SageMakerAlarmModel


class SageMakerAutoRollbackConfigModel(BaseModel):
    Alarms: list[SageMakerAlarmModel] | None = None
