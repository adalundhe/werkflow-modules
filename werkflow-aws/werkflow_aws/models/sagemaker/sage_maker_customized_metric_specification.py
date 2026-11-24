from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerCustomizedMetricSpecification(BaseModel):
    MetricName: StrictStr | None = None
    Namespace: StrictStr | None = None
    Statistic: StrictStr | None = None
