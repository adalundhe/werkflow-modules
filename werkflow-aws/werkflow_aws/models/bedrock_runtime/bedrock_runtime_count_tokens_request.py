from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_count_tokens_input import BedrockRuntimeCountTokensInput


class BedrockRuntimeCountTokensRequest(BaseModel):
    modelId: StrictStr
    input: BedrockRuntimeCountTokensInput
