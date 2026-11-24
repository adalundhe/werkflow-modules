from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_runtime_converse_stream_output import BedrockRuntimeConverseStreamOutput


class BedrockRuntimeConverseStreamResponse(BaseModel):
    stream: BedrockRuntimeConverseStreamOutput | None = None
    ResponseMetadata: dict[str, Any] | None = None
