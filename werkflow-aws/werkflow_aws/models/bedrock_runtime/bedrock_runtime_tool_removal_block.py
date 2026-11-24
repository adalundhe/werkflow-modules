from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_tool_reference import BedrockRuntimeToolReference


class BedrockRuntimeToolRemovalBlock(BaseModel):
    tool: BedrockRuntimeToolReference | None = None
