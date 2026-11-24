from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_customization_config import BedrockCustomizationConfig
from .bedrock_output_data_config import BedrockOutputDataConfig
from .bedrock_status_details import BedrockStatusDetails
from .bedrock_training_data_config import BedrockTrainingDataConfig
from .bedrock_training_metrics import BedrockTrainingMetrics
from .bedrock_validation_data_config import BedrockValidationDataConfig
from .bedrock_validator_metric import BedrockValidatorMetric
from .bedrock_vpc_config import BedrockVpcConfig


class BedrockGetModelCustomizationJobResponse(BaseModel):
    jobArn: StrictStr | None = None
    jobName: StrictStr | None = None
    outputModelName: StrictStr | None = None
    outputModelArn: StrictStr | None = None
    clientRequestToken: StrictStr | None = None
    roleArn: StrictStr | None = None
    status: StrictStr | None = None
    statusDetails: BedrockStatusDetails | None = None
    failureMessage: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastModifiedTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
    baseModelArn: StrictStr | None = None
    hyperParameters: dict[StrictStr, StrictStr] | None = None
    trainingDataConfig: BedrockTrainingDataConfig | None = None
    validationDataConfig: BedrockValidationDataConfig | None = None
    outputDataConfig: BedrockOutputDataConfig | None = None
    customizationType: StrictStr | None = None
    outputModelKmsKeyArn: StrictStr | None = None
    trainingMetrics: BedrockTrainingMetrics | None = None
    validationMetrics: list[BedrockValidatorMetric] | None = None
    vpcConfig: BedrockVpcConfig | None = None
    customizationConfig: BedrockCustomizationConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
