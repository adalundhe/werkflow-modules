from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_document import BedrockRuntimeDocument


class BedrockRuntimeToolUseBlock(BaseModel):
    toolUseId: StrictStr | None = None
    name: StrictStr | None = None
    input: BedrockRuntimeDocument | None = None
    type: StrictStr | None = None
