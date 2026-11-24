from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_guardrail_image_coverage import BedrockRuntimeGuardrailImageCoverage
from .bedrock_runtime_guardrail_text_characters_coverage import BedrockRuntimeGuardrailTextCharactersCoverage


class BedrockRuntimeGuardrailCoverage(BaseModel):
    textCharacters: BedrockRuntimeGuardrailTextCharactersCoverage | None = None
    images: BedrockRuntimeGuardrailImageCoverage | None = None
