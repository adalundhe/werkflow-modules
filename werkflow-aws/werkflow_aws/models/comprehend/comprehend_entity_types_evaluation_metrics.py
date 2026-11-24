from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class ComprehendEntityTypesEvaluationMetrics(BaseModel):
    Precision: StrictFloat | StrictInt | None = None
    Recall: StrictFloat | StrictInt | None = None
    F1Score: StrictFloat | StrictInt | None = None
