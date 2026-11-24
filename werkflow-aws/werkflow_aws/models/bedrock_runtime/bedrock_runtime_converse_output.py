from __future__ import annotations
from pydantic import BaseModel
from .bedrock_runtime_message import BedrockRuntimeMessage


class BedrockRuntimeConverseOutput(BaseModel):
    message: BedrockRuntimeMessage | None = None
