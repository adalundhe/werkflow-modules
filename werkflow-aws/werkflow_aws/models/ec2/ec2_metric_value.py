from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class EC2MetricValue(BaseModel):
    Metric: StrictStr | None = None
    Value: StrictFloat | StrictInt | None = None
