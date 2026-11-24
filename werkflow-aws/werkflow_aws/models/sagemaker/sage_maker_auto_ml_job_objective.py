from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAutoMLJobObjective(BaseModel):
    MetricName: StrictStr | None = None
