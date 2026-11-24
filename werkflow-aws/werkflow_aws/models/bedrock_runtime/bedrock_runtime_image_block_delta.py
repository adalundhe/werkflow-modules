from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_error_block import BedrockRuntimeErrorBlock
from .bedrock_runtime_image_source import BedrockRuntimeImageSource


class BedrockRuntimeImageBlockDelta(BaseModel):
    source: BedrockRuntimeImageSource | None = None
    error: BedrockRuntimeErrorBlock | None = None
