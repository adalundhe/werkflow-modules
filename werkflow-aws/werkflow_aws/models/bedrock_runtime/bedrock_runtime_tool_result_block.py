from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_tool_result_content_block import BedrockRuntimeToolResultContentBlock


class BedrockRuntimeToolResultBlock(BaseModel):
    toolUseId: StrictStr | None = None
    content: list[BedrockRuntimeToolResultContentBlock] | None = None
    status: StrictStr | None = None
    type: StrictStr | None = None
