from __future__ import annotations
from pydantic import BaseModel
from .rekognition_detect_labels_image_background import RekognitionDetectLabelsImageBackground
from .rekognition_detect_labels_image_foreground import RekognitionDetectLabelsImageForeground
from .rekognition_detect_labels_image_quality import RekognitionDetectLabelsImageQuality
from .rekognition_dominant_color import RekognitionDominantColor


class RekognitionDetectLabelsImageProperties(BaseModel):
    Quality: RekognitionDetectLabelsImageQuality | None = None
    DominantColors: list[RekognitionDominantColor] | None = None
    Foreground: RekognitionDetectLabelsImageForeground | None = None
    Background: RekognitionDetectLabelsImageBackground | None = None
