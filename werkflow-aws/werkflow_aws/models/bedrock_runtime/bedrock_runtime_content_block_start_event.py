from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .bedrock_runtime_content_block_start import BedrockRuntimeContentBlockStart


class BedrockRuntimeContentBlockStartEvent(BaseModel):
    start: BedrockRuntimeContentBlockStart | None = None
    contentBlockIndex: StrictInt | None = None
