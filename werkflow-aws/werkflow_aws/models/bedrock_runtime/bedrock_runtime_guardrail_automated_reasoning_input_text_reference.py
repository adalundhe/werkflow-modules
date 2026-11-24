from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeGuardrailAutomatedReasoningInputTextReference(BaseModel):
    text: StrictStr | None = None
