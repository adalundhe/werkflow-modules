from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .bedrock_runtime_cache_detail import BedrockRuntimeCacheDetail


class BedrockRuntimeTokenUsage(BaseModel):
    inputTokens: StrictInt | None = None
    outputTokens: StrictInt | None = None
    totalTokens: StrictInt | None = None
    cacheReadInputTokens: StrictInt | None = None
    cacheWriteInputTokens: StrictInt | None = None
    cacheDetails: list[BedrockRuntimeCacheDetail] | None = None
