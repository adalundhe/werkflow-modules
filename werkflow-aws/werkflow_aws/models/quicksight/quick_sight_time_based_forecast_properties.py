from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class QuickSightTimeBasedForecastProperties(BaseModel):
    PeriodsForward: StrictInt | None = None
    PeriodsBackward: StrictInt | None = None
    UpperBoundary: StrictFloat | StrictInt | None = None
    LowerBoundary: StrictFloat | StrictInt | None = None
    PredictionInterval: StrictInt | None = None
    Seasonality: StrictInt | None = None
