from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimePromptRouterTrace(BaseModel):
    invokedModelId: StrictStr | None = None
