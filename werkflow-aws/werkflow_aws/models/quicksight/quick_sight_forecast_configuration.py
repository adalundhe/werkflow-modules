from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_forecast_scenario import QuickSightForecastScenario
from .quick_sight_time_based_forecast_properties import QuickSightTimeBasedForecastProperties


class QuickSightForecastConfiguration(BaseModel):
    ForecastProperties: QuickSightTimeBasedForecastProperties | None = None
    Scenario: QuickSightForecastScenario | None = None
