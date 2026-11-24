from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .bedrock_customization_config import BedrockCustomizationConfig
from .bedrock_output_data_config import BedrockOutputDataConfig
from .bedrock_tag import BedrockTag
from .bedrock_training_data_config import BedrockTrainingDataConfig
from .bedrock_validation_data_config import BedrockValidationDataConfig
from .bedrock_vpc_config import BedrockVpcConfig


class BedrockCreateModelCustomizationJobRequest(BaseModel):
    jobName: StrictStr
    customModelName: StrictStr
    roleArn: StrictStr
    baseModelIdentifier: StrictStr
    trainingDataConfig: BedrockTrainingDataConfig
    outputDataConfig: BedrockOutputDataConfig
    clientRequestToken: StrictStr | None = None
    customizationType: Literal['FINE_TUNING', 'CONTINUED_PRE_TRAINING', 'DISTILLATION', 'REINFORCEMENT_FINE_TUNING', 'IMPORTED'] | None = None
    customModelKmsKeyId: StrictStr | None = None
    jobTags: list[BedrockTag] | None = None
    customModelTags: list[BedrockTag] | None = None
    validationDataConfig: BedrockValidationDataConfig | None = None
    hyperParameters: dict[StrictStr, StrictStr] | None = None
    vpcConfig: BedrockVpcConfig | None = None
    customizationConfig: BedrockCustomizationConfig | None = None
