from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class ComprehendClassifierEvaluationMetrics(BaseModel):
    Accuracy: StrictFloat | StrictInt | None = None
    Precision: StrictFloat | StrictInt | None = None
    Recall: StrictFloat | StrictInt | None = None
    F1Score: StrictFloat | StrictInt | None = None
    MicroPrecision: StrictFloat | StrictInt | None = None
    MicroRecall: StrictFloat | StrictInt | None = None
    MicroF1Score: StrictFloat | StrictInt | None = None
    HammingLoss: StrictFloat | StrictInt | None = None
