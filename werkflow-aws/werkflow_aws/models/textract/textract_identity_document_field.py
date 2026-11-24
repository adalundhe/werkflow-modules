from __future__ import annotations
from pydantic import BaseModel
from .textract_analyze_id_detections import TextractAnalyzeIDDetections


class TextractIdentityDocumentField(BaseModel):
    Type: TextractAnalyzeIDDetections | None = None
    ValueDetection: TextractAnalyzeIDDetections | None = None
