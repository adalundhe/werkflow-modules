from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_advanced_prompt_optimization_input_config import BedrockAdvancedPromptOptimizationInputConfig
from .bedrock_advanced_prompt_optimization_output_config import BedrockAdvancedPromptOptimizationOutputConfig
from .bedrock_model_configuration import BedrockModelConfiguration


class BedrockGetAdvancedPromptOptimizationJobResponse(BaseModel):
    jobArn: StrictStr | None = None
    jobName: StrictStr | None = None
    jobDescription: StrictStr | None = None
    jobStatus: StrictStr | None = None
    inputConfig: BedrockAdvancedPromptOptimizationInputConfig | None = None
    outputConfig: BedrockAdvancedPromptOptimizationOutputConfig | None = None
    encryptionKeyArn: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastModifiedTime: datetime.datetime | StrictStr | None = None
    failureMessage: StrictStr | None = None
    modelConfigurations: list[BedrockModelConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
