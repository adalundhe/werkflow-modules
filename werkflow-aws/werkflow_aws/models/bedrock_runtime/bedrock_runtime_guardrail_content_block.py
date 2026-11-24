from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_guardrail_image_block import BedrockRuntimeGuardrailImageBlock
from .bedrock_runtime_guardrail_text_block import BedrockRuntimeGuardrailTextBlock


class BedrockRuntimeGuardrailContentBlock(BaseModel):
    text: BedrockRuntimeGuardrailTextBlock | None = None
    image: BedrockRuntimeGuardrailImageBlock | None = None
