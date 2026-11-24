from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_tag import BedrockTag


class BedrockListTagsForResourceResponse(BaseModel):
    tags: list[BedrockTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
