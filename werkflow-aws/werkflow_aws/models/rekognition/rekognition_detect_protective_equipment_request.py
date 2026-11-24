from __future__ import annotations
from pydantic import BaseModel
from .rekognition_image import RekognitionImage
from .rekognition_protective_equipment_summarization_attributes import RekognitionProtectiveEquipmentSummarizationAttributes


class RekognitionDetectProtectiveEquipmentRequest(BaseModel):
    Image: RekognitionImage
    SummarizationAttributes: RekognitionProtectiveEquipmentSummarizationAttributes | None = None
