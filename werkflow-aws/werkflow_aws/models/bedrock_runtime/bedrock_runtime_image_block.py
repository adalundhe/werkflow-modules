from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_error_block import BedrockRuntimeErrorBlock
from .bedrock_runtime_image_source import BedrockRuntimeImageSource


class BedrockRuntimeImageBlock(BaseModel):
    format: StrictStr | None = None
    source: BedrockRuntimeImageSource | None = None
    error: BedrockRuntimeErrorBlock | None = None
