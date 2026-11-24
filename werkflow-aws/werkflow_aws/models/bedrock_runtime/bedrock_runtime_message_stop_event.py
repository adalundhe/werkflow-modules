from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_runtime_document import BedrockRuntimeDocument


class BedrockRuntimeMessageStopEvent(BaseModel):
    stopReason: StrictStr | None = None
    additionalModelResponseFields: BedrockRuntimeDocument | None = None
