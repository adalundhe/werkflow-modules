from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_tool_reference import BedrockRuntimeToolReference


class BedrockRuntimeToolAdditionBlock(BaseModel):
    tool: BedrockRuntimeToolReference | None = None
