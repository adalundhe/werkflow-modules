from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .bedrock_runtime_guardrail_image_source import BedrockRuntimeGuardrailImageSource


class BedrockRuntimeGuardrailImageBlock(BaseModel):
    format: Literal['png', 'jpeg']
    source: BedrockRuntimeGuardrailImageSource
