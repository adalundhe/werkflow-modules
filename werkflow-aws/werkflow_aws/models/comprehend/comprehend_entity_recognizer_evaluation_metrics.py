from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class ComprehendEntityRecognizerEvaluationMetrics(BaseModel):
    Precision: StrictFloat | StrictInt | None = None
    Recall: StrictFloat | StrictInt | None = None
    F1Score: StrictFloat | StrictInt | None = None
