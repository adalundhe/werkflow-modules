from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_response_stream import BedrockRuntimeResponseStream


class BedrockRuntimeInvokeModelWithResponseStreamResponse(BaseModel):
    body: BedrockRuntimeResponseStream | None = None
    contentType: StrictStr | None = None
    performanceConfigLatency: StrictStr | None = None
    serviceTier: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
