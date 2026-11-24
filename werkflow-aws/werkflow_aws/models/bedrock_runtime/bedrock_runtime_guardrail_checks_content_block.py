from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeGuardrailChecksContentBlock(BaseModel):
    text: StrictStr | None = None
