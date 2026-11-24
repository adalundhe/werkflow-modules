from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .time_period import TimePeriod as CETimePeriod


class CostExplorerForecastResult(BaseModel):
    TimePeriod: CETimePeriod | None = None
    MeanValue: StrictStr | None = None
    PredictionIntervalLowerBound: StrictStr | None = None
    PredictionIntervalUpperBound: StrictStr | None = None
