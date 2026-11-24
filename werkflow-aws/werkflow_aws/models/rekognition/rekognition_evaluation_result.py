from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .rekognition_summary import RekognitionSummary


class RekognitionEvaluationResult(BaseModel):
    F1Score: StrictFloat | StrictInt | None = None
    Summary: RekognitionSummary | None = None
