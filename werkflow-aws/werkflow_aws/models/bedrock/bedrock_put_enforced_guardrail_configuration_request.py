from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_account_enforced_guardrail_inference_input_configuration import BedrockAccountEnforcedGuardrailInferenceInputConfiguration


class BedrockPutEnforcedGuardrailConfigurationRequest(BaseModel):
    guardrailInferenceConfig: BedrockAccountEnforcedGuardrailInferenceInputConfiguration
    configId: StrictStr | None = None
