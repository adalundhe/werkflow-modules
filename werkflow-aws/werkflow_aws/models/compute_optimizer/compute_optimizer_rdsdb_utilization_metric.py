from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComputeOptimizerRDSDBUtilizationMetric(BaseModel):
    name: StrictStr | None = None
    statistic: StrictStr | None = None
    value: StrictFloat | StrictInt | None = None
