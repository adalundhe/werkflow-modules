from __future__ import annotations
from pydantic import BaseModel
from .rekognition_testing_data import RekognitionTestingData
from .rekognition_validation_data import RekognitionValidationData


class RekognitionTestingDataResult(BaseModel):
    Input: RekognitionTestingData | None = None
    Output: RekognitionTestingData | None = None
    Validation: RekognitionValidationData | None = None
