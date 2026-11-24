from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SageMakerMetricDatum(BaseModel):
    MetricName: StrictStr | None = None
    StandardMetricName: StrictStr | None = None
    Value: StrictFloat | StrictInt | None = None
    Set: StrictStr | None = None
