from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_image_block_start import BedrockRuntimeImageBlockStart
from .bedrock_runtime_tool_result_block_start import BedrockRuntimeToolResultBlockStart
from .bedrock_runtime_tool_use_block_start import BedrockRuntimeToolUseBlockStart


class BedrockRuntimeContentBlockStart(BaseModel):
    toolUse: BedrockRuntimeToolUseBlockStart | None = None
    toolResult: BedrockRuntimeToolResultBlockStart | None = None
    image: BedrockRuntimeImageBlockStart | None = None
