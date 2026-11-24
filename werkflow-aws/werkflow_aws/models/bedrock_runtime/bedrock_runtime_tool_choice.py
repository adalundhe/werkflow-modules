from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_any_tool_choice import BedrockRuntimeAnyToolChoice
from .bedrock_runtime_auto_tool_choice import BedrockRuntimeAutoToolChoice
from .bedrock_runtime_specific_tool_choice import BedrockRuntimeSpecificToolChoice


class BedrockRuntimeToolChoice(BaseModel):
    auto: BedrockRuntimeAutoToolChoice | None = None
    any: BedrockRuntimeAnyToolChoice | None = None
    tool: BedrockRuntimeSpecificToolChoice | None = None
