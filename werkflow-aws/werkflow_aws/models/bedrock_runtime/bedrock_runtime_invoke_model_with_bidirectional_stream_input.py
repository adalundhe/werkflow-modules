from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_bidirectional_input_payload_part import BedrockRuntimeBidirectionalInputPayloadPart


class BedrockRuntimeInvokeModelWithBidirectionalStreamInput(BaseModel):
    chunk: BedrockRuntimeBidirectionalInputPayloadPart | None = None
