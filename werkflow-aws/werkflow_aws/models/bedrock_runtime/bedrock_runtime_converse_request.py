from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_document import BedrockRuntimeDocument
from .bedrock_runtime_guardrail_configuration import BedrockRuntimeGuardrailConfiguration
from .bedrock_runtime_inference_configuration import BedrockRuntimeInferenceConfiguration
from .bedrock_runtime_message import BedrockRuntimeMessage
from .bedrock_runtime_output_config import BedrockRuntimeOutputConfig
from .bedrock_runtime_performance_configuration import BedrockRuntimePerformanceConfiguration
from .bedrock_runtime_prompt_variable_values import BedrockRuntimePromptVariableValues
from .bedrock_runtime_service_tier import BedrockRuntimeServiceTier
from .bedrock_runtime_system_content_block import BedrockRuntimeSystemContentBlock
from .bedrock_runtime_tool_configuration import BedrockRuntimeToolConfiguration


class BedrockRuntimeConverseRequest(BaseModel):
    modelId: StrictStr
    messages: list[BedrockRuntimeMessage] | None = None
    system: list[BedrockRuntimeSystemContentBlock] | None = None
    inferenceConfig: BedrockRuntimeInferenceConfiguration | None = None
    toolConfig: BedrockRuntimeToolConfiguration | None = None
    guardrailConfig: BedrockRuntimeGuardrailConfiguration | None = None
    projectIdentifier: StrictStr | None = None
    additionalModelRequestFields: BedrockRuntimeDocument | None = None
    promptVariables: dict[StrictStr, BedrockRuntimePromptVariableValues] | None = None
    additionalModelResponseFieldPaths: list[StrictStr] | None = None
    requestMetadata: dict[StrictStr, StrictStr] | None = None
    performanceConfig: BedrockRuntimePerformanceConfiguration | None = None
    serviceTier: BedrockRuntimeServiceTier | None = None
    outputConfig: BedrockRuntimeOutputConfig | None = None
