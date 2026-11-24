from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComputeOptimizerECSServiceProjectedUtilizationMetric(BaseModel):
    name: StrictStr | None = None
    statistic: StrictStr | None = None
    lowerBoundValue: StrictFloat | StrictInt | None = None
    upperBoundValue: StrictFloat | StrictInt | None = None
