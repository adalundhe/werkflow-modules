from __future__ import annotations
from pydantic import BaseModel
from .rekognition_detect_labels_image_properties_settings import RekognitionDetectLabelsImagePropertiesSettings
from .rekognition_general_labels_settings import RekognitionGeneralLabelsSettings


class RekognitionDetectLabelsSettings(BaseModel):
    GeneralLabels: RekognitionGeneralLabelsSettings | None = None
    ImageProperties: RekognitionDetectLabelsImagePropertiesSettings | None = None
