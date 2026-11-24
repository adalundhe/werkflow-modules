from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_model_enforcement import BedrockModelEnforcement
from .bedrock_selective_content_guarding import BedrockSelectiveContentGuarding


class BedrockAccountEnforcedGuardrailInferenceInputConfiguration(BaseModel):
    guardrailIdentifier: StrictStr
    guardrailVersion: StrictStr
    selectiveContentGuarding: BedrockSelectiveContentGuarding | None = None
    modelEnforcement: BedrockModelEnforcement | None = None
