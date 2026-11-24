from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BedrockTextInferenceConfig(BaseModel):
    temperature: StrictFloat | StrictInt | None = None
    topP: StrictFloat | StrictInt | None = None
    maxTokens: StrictInt | None = None
    stopSequences: list[StrictStr] | None = None
