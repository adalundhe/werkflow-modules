from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt
from .rekognition_detect_labels_settings import RekognitionDetectLabelsSettings
from .rekognition_image import RekognitionImage


class RekognitionDetectLabelsRequest(BaseModel):
    Image: RekognitionImage
    MaxLabels: StrictInt | None = None
    MinConfidence: StrictFloat | StrictInt | None = None
    Features: list[Literal['GENERAL_LABELS', 'IMAGE_PROPERTIES']] | None = None
    Settings: RekognitionDetectLabelsSettings | None = None
