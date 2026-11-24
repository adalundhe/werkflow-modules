from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeGuardrailConverseTextBlock(BaseModel):
    text: StrictStr | None = None
    qualifiers: list[StrictStr] | None = None
