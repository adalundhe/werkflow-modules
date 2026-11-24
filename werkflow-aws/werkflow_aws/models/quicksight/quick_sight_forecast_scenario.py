from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_what_if_point_scenario import QuickSightWhatIfPointScenario
from .quick_sight_what_if_range_scenario import QuickSightWhatIfRangeScenario


class QuickSightForecastScenario(BaseModel):
    WhatIfPointScenario: QuickSightWhatIfPointScenario | None = None
    WhatIfRangeScenario: QuickSightWhatIfRangeScenario | None = None
