from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .rekognition_text_detection import RekognitionTextDetection


class RekognitionTextDetectionResult(BaseModel):
    Timestamp: StrictInt | None = None
    TextDetection: RekognitionTextDetection | None = None
