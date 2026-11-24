from __future__ import annotations
from pydantic import BaseModel
from .bedrock_data_processing_details import BedrockDataProcessingDetails
from .bedrock_training_details import BedrockTrainingDetails
from .bedrock_validation_details import BedrockValidationDetails


class BedrockStatusDetails(BaseModel):
    validationDetails: BedrockValidationDetails | None = None
    dataProcessingDetails: BedrockDataProcessingDetails | None = None
    trainingDetails: BedrockTrainingDetails | None = None
