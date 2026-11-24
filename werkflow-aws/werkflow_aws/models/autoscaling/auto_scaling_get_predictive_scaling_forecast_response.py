from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .auto_scaling_capacity_forecast import AutoScalingCapacityForecast
from .auto_scaling_load_forecast import AutoScalingLoadForecast


class AutoScalingGetPredictiveScalingForecastResponse(BaseModel):
    LoadForecast: list[AutoScalingLoadForecast] | None = None
    CapacityForecast: AutoScalingCapacityForecast | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
