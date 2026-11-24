from __future__ import annotations
from pydantic import BaseModel
from .rekognition_general_labels_settings import RekognitionGeneralLabelsSettings


class RekognitionLabelDetectionSettings(BaseModel):
    GeneralLabels: RekognitionGeneralLabelsSettings | None = None
