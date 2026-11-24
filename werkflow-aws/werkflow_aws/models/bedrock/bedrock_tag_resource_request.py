from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_tag import BedrockTag


class BedrockTagResourceRequest(BaseModel):
    resourceARN: StrictStr
    tags: list[BedrockTag]
