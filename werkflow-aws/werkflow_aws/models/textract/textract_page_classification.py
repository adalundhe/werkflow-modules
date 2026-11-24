from __future__ import annotations
from pydantic import BaseModel
from .textract_prediction import TextractPrediction


class TextractPageClassification(BaseModel):
    PageType: list[TextractPrediction] | None = None
    PageNumber: list[TextractPrediction] | None = None
