from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class ComprehendFlywheelModelEvaluationMetrics(BaseModel):
    AverageF1Score: StrictFloat | StrictInt | None = None
    AveragePrecision: StrictFloat | StrictInt | None = None
    AverageRecall: StrictFloat | StrictInt | None = None
    AverageAccuracy: StrictFloat | StrictInt | None = None
