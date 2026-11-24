from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerPredefinedMetricSpecification(BaseModel):
    PredefinedMetricType: StrictStr | None = None
