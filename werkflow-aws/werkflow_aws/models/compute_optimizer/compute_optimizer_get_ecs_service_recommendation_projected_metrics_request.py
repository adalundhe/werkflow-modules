from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class ComputeOptimizerGetECSServiceRecommendationProjectedMetricsRequest(BaseModel):
    serviceArn: StrictStr
    stat: Literal['Maximum', 'Average']
    period: StrictInt
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
