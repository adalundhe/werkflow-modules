from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_video_source import BedrockRuntimeVideoSource


class BedrockRuntimeVideoBlock(BaseModel):
    format: StrictStr | None = None
    source: BedrockRuntimeVideoSource | None = None
