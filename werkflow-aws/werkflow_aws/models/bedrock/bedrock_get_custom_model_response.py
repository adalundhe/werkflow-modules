from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_customization_config import BedrockCustomizationConfig
from .bedrock_output_data_config import BedrockOutputDataConfig
from .bedrock_training_data_config import BedrockTrainingDataConfig
from .bedrock_training_metrics import BedrockTrainingMetrics
from .bedrock_validation_data_config import BedrockValidationDataConfig
from .bedrock_validator_metric import BedrockValidatorMetric


class BedrockGetCustomModelResponse(BaseModel):
    modelArn: StrictStr | None = None
    modelName: StrictStr | None = None
    jobName: StrictStr | None = None
    jobArn: StrictStr | None = None
    baseModelArn: StrictStr | None = None
    customizationType: StrictStr | None = None
    modelKmsKeyArn: StrictStr | None = None
    hyperParameters: dict[StrictStr, StrictStr] | None = None
    trainingDataConfig: BedrockTrainingDataConfig | None = None
    validationDataConfig: BedrockValidationDataConfig | None = None
    outputDataConfig: BedrockOutputDataConfig | None = None
    trainingMetrics: BedrockTrainingMetrics | None = None
    validationMetrics: list[BedrockValidatorMetric] | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    customizationConfig: BedrockCustomizationConfig | None = None
    modelStatus: StrictStr | None = None
    failureMessage: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
