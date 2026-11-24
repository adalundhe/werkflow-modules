from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class TextractEvaluationMetric(BaseModel):
    F1Score: StrictFloat | StrictInt | None = None
    Precision: StrictFloat | StrictInt | None = None
    Recall: StrictFloat | StrictInt | None = None
