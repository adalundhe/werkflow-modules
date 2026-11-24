from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_tool import BedrockRuntimeTool
from .bedrock_runtime_tool_choice import BedrockRuntimeToolChoice


class BedrockRuntimeToolConfiguration(BaseModel):
    tools: list[BedrockRuntimeTool]
    toolChoice: BedrockRuntimeToolChoice | None = None
