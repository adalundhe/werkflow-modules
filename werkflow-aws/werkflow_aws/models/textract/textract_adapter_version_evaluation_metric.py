from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .textract_evaluation_metric import TextractEvaluationMetric


class TextractAdapterVersionEvaluationMetric(BaseModel):
    Baseline: TextractEvaluationMetric | None = None
    AdapterVersion: TextractEvaluationMetric | None = None
    FeatureType: StrictStr | None = None
