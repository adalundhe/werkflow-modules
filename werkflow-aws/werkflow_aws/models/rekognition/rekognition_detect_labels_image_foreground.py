from __future__ import annotations
from pydantic import BaseModel
from .rekognition_detect_labels_image_quality import RekognitionDetectLabelsImageQuality
from .rekognition_dominant_color import RekognitionDominantColor


class RekognitionDetectLabelsImageForeground(BaseModel):
    Quality: RekognitionDetectLabelsImageQuality | None = None
    DominantColors: list[RekognitionDominantColor] | None = None
