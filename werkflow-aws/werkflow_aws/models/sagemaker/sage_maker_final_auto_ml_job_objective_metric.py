from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SageMakerFinalAutoMLJobObjectiveMetric(BaseModel):
    Type: StrictStr | None = None
    MetricName: StrictStr | None = None
    Value: StrictFloat | StrictInt | None = None
    StandardMetricName: StrictStr | None = None
