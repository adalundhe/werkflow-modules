from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_guardrail_converse_image_source import BedrockRuntimeGuardrailConverseImageSource


class BedrockRuntimeGuardrailConverseImageBlock(BaseModel):
    format: StrictStr | None = None
    source: BedrockRuntimeGuardrailConverseImageSource | None = None
