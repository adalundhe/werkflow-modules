from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_converse_tokens_request import BedrockRuntimeConverseTokensRequest
from .bedrock_runtime_invoke_model_tokens_request import BedrockRuntimeInvokeModelTokensRequest


class BedrockRuntimeCountTokensInput(BaseModel):
    invokeModel: BedrockRuntimeInvokeModelTokensRequest | None = None
    converse: BedrockRuntimeConverseTokensRequest | None = None
