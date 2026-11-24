from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_idle_dimension import ComputeOptimizerIdleDimension


class ComputeOptimizerIdleUtilizationMetric(BaseModel):
    name: StrictStr | None = None
    statistic: StrictStr | None = None
    value: StrictFloat | StrictInt | None = None
    dimensions: list[ComputeOptimizerIdleDimension] | None = None
