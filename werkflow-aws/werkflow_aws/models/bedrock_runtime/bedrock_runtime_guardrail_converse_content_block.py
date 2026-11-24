from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_guardrail_converse_image_block import BedrockRuntimeGuardrailConverseImageBlock
from .bedrock_runtime_guardrail_converse_text_block import BedrockRuntimeGuardrailConverseTextBlock


class BedrockRuntimeGuardrailConverseContentBlock(BaseModel):
    text: BedrockRuntimeGuardrailConverseTextBlock | None = None
    image: BedrockRuntimeGuardrailConverseImageBlock | None = None
