from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockRuntimeGuardrailContentFilter(BaseModel):
    type: StrictStr | None = None
    confidence: StrictStr | None = None
    filterStrength: StrictStr | None = None
    action: StrictStr | None = None
    detected: StrictBool | None = None
