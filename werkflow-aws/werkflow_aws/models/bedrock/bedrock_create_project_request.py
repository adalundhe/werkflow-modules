from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_project_data_retention import BedrockProjectDataRetention
from .bedrock_tag import BedrockTag


class BedrockCreateProjectRequest(BaseModel):
    name: StrictStr
    tags: list[BedrockTag] | None = None
    dataRetention: BedrockProjectDataRetention | None = None
