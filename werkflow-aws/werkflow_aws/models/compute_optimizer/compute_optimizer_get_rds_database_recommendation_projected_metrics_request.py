from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_recommendation_preferences import ComputeOptimizerRecommendationPreferences


class ComputeOptimizerGetRDSDatabaseRecommendationProjectedMetricsRequest(BaseModel):
    resourceArn: StrictStr
    stat: Literal['Maximum', 'Average']
    period: StrictInt
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr
    recommendationPreferences: ComputeOptimizerRecommendationPreferences | None = None
