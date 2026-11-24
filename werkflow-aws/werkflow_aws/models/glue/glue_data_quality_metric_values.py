from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class GlueDataQualityMetricValues(BaseModel):
    ActualValue: StrictFloat | StrictInt | None = None
    ExpectedValue: StrictFloat | StrictInt | None = None
    LowerLimit: StrictFloat | StrictInt | None = None
    UpperLimit: StrictFloat | StrictInt | None = None
