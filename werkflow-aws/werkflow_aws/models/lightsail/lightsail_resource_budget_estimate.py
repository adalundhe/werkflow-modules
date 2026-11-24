from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lightsail_cost_estimate import LightsailCostEstimate


class LightsailResourceBudgetEstimate(BaseModel):
    resourceName: StrictStr | None = None
    resourceType: StrictStr | None = None
    costEstimates: list[LightsailCostEstimate] | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
