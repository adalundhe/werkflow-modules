from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cost_explorer_date_interval import CostExplorerDateInterval


class CostExplorerForecastResultModel(BaseModel):
    TimePeriod: CostExplorerDateInterval | None = None
    MeanValue: StrictStr | None = None
    PredictionIntervalLowerBound: StrictStr | None = None
    PredictionIntervalUpperBound: StrictStr | None = None
