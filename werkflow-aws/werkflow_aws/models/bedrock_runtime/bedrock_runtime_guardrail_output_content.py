from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeGuardrailOutputContent(BaseModel):
    text: StrictStr | None = None
