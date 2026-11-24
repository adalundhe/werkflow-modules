from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_content_block import BedrockRuntimeContentBlock


class BedrockRuntimeMessage(BaseModel):
    role: StrictStr | None = None
    content: list[BedrockRuntimeContentBlock] | None = None
