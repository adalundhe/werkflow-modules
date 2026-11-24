from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_audio_source import BedrockRuntimeAudioSource
from .bedrock_runtime_error_block import BedrockRuntimeErrorBlock


class BedrockRuntimeAudioBlock(BaseModel):
    format: StrictStr | None = None
    source: BedrockRuntimeAudioSource | None = None
    error: BedrockRuntimeErrorBlock | None = None
