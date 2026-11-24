from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt


class BedrockRuntimeCountTokensResponse(BaseModel):
    inputTokens: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
