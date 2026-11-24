from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeReasoningTextBlock(BaseModel):
    text: StrictStr | None = None
    signature: StrictStr | None = None
