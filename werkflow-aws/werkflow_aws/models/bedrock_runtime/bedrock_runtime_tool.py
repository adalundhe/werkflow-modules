from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_cache_point_block import BedrockRuntimeCachePointBlock
from .bedrock_runtime_system_tool import BedrockRuntimeSystemTool
from .bedrock_runtime_tool_specification import BedrockRuntimeToolSpecification


class BedrockRuntimeTool(BaseModel):
    toolSpec: BedrockRuntimeToolSpecification | None = None
    systemTool: BedrockRuntimeSystemTool | None = None
    cachePoint: BedrockRuntimeCachePointBlock | None = None
