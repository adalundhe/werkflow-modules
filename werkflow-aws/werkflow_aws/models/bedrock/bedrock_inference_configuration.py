from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BedrockInferenceConfiguration(BaseModel):
    maxTokens: StrictInt | None = None
    temperature: StrictFloat | StrictInt | None = None
    topP: StrictFloat | StrictInt | None = None
    stopSequences: list[StrictStr] | None = None
