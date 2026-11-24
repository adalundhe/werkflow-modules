from __future__ import annotations
from pydantic import BaseModel
from .bedrock_text_inference_config import BedrockTextInferenceConfig


class BedrockKbInferenceConfig(BaseModel):
    textInferenceConfig: BedrockTextInferenceConfig | None = None
