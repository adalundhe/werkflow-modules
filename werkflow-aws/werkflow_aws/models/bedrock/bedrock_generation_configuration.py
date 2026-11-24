from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_additional_model_request_fields_value import BedrockAdditionalModelRequestFieldsValue
from .bedrock_guardrail_configuration import BedrockGuardrailConfiguration
from .bedrock_kb_inference_config import BedrockKbInferenceConfig
from .bedrock_prompt_template import BedrockPromptTemplate


class BedrockGenerationConfiguration(BaseModel):
    promptTemplate: BedrockPromptTemplate | None = None
    guardrailConfiguration: BedrockGuardrailConfiguration | None = None
    kbInferenceConfig: BedrockKbInferenceConfig | None = None
    additionalModelRequestFields: dict[StrictStr, BedrockAdditionalModelRequestFieldsValue] | None = None
