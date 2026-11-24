from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_runtime_invoke_model_with_bidirectional_stream_output import BedrockRuntimeInvokeModelWithBidirectionalStreamOutput


class BedrockRuntimeInvokeModelWithBidirectionalStreamResponse(BaseModel):
    body: BedrockRuntimeInvokeModelWithBidirectionalStreamOutput | None = None
    ResponseMetadata: dict[str, Any] | None = None
