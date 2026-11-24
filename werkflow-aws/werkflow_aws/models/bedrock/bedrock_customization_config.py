from __future__ import annotations
from pydantic import BaseModel
from .bedrock_distillation_config import BedrockDistillationConfig
from .bedrock_rft_config import BedrockRFTConfig


class BedrockCustomizationConfig(BaseModel):
    distillationConfig: BedrockDistillationConfig | None = None
    rftConfig: BedrockRFTConfig | None = None
