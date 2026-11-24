from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .bedrock_runtime_content_block_delta import BedrockRuntimeContentBlockDelta


class BedrockRuntimeContentBlockDeltaEvent(BaseModel):
    delta: BedrockRuntimeContentBlockDelta | None = None
    contentBlockIndex: StrictInt | None = None
