from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_advanced_prompt_optimization_input_config import BedrockAdvancedPromptOptimizationInputConfig
from .bedrock_advanced_prompt_optimization_output_config import BedrockAdvancedPromptOptimizationOutputConfig
from .bedrock_model_configuration import BedrockModelConfiguration
from .bedrock_tag import BedrockTag


class BedrockCreateAdvancedPromptOptimizationJobRequest(BaseModel):
    jobName: StrictStr
    inputConfig: BedrockAdvancedPromptOptimizationInputConfig
    outputConfig: BedrockAdvancedPromptOptimizationOutputConfig
    modelConfigurations: list[BedrockModelConfiguration]
    jobDescription: StrictStr | None = None
    clientToken: StrictStr | None = None
    encryptionKeyArn: StrictStr | None = None
    tags: list[BedrockTag] | None = None
