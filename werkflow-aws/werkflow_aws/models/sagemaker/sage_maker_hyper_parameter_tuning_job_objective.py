from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerHyperParameterTuningJobObjective(BaseModel):
    Type: StrictStr | None = None
    MetricName: StrictStr | None = None
