from __future__ import annotations
from pydantic import BaseModel
from .rekognition_detect_text_filters import RekognitionDetectTextFilters
from .rekognition_image import RekognitionImage


class RekognitionDetectTextRequest(BaseModel):
    Image: RekognitionImage
    Filters: RekognitionDetectTextFilters | None = None
