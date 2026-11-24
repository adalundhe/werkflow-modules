from __future__ import annotations
from pydantic import BaseModel, StrictInt


class IoTDetectMitigationActionsTaskStatistics(BaseModel):
    actionsExecuted: StrictInt | None = None
    actionsSkipped: StrictInt | None = None
    actionsFailed: StrictInt | None = None
