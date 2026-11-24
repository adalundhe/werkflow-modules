from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_cache_point_block import BedrockRuntimeCachePointBlock
from .bedrock_runtime_guardrail_converse_content_block import BedrockRuntimeGuardrailConverseContentBlock


class BedrockRuntimeSystemContentBlock(BaseModel):
    text: StrictStr | None = None
    guardContent: BedrockRuntimeGuardrailConverseContentBlock | None = None
    cachePoint: BedrockRuntimeCachePointBlock | None = None
