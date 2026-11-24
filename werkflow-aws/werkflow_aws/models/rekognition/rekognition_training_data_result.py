from __future__ import annotations
from pydantic import BaseModel
from .rekognition_training_data import RekognitionTrainingData
from .rekognition_validation_data import RekognitionValidationData


class RekognitionTrainingDataResult(BaseModel):
    Input: RekognitionTrainingData | None = None
    Output: RekognitionTrainingData | None = None
    Validation: RekognitionValidationData | None = None
