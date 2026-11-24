from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .comprehend_classifier_evaluation_metrics import ComprehendClassifierEvaluationMetrics


class ComprehendClassifierMetadata(BaseModel):
    NumberOfLabels: StrictInt | None = None
    NumberOfTrainedDocuments: StrictInt | None = None
    NumberOfTestDocuments: StrictInt | None = None
    EvaluationMetrics: ComprehendClassifierEvaluationMetrics | None = None
