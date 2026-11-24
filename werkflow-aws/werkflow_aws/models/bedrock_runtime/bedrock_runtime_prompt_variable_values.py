from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimePromptVariableValues(BaseModel):
    text: StrictStr | None = None
