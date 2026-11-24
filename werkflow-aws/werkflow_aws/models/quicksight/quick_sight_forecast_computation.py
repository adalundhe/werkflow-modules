from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_measure_field import QuickSightMeasureField


class QuickSightForecastComputation(BaseModel):
    ComputationId: StrictStr | None = None
    Name: StrictStr | None = None
    Time: QuickSightDimensionField | None = None
    Value: QuickSightMeasureField | None = None
    PeriodsForward: StrictInt | None = None
    PeriodsBackward: StrictInt | None = None
    UpperBoundary: StrictFloat | StrictInt | None = None
    LowerBoundary: StrictFloat | StrictInt | None = None
    PredictionInterval: StrictInt | None = None
    Seasonality: StrictStr | None = None
    CustomSeasonalityValue: StrictInt | None = None
