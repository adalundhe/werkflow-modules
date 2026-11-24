from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .bedrock_runtime_document import BedrockRuntimeDocument


class BedrockRuntimeToolInputSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    json_: BedrockRuntimeDocument | None = Field(default=None, alias='json')
