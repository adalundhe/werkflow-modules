from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEvaluationFormMetricConfiguration(BaseModel):
    MetricType: StrictStr | None = None
    MetricName: StrictStr | None = None
