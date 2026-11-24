from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from .bedrock_runtime_document import BedrockRuntimeDocument


class BedrockRuntimeToolResultBlockDelta(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    text: StrictStr | None = None
    json_: BedrockRuntimeDocument | None = Field(default=None, alias='json')
