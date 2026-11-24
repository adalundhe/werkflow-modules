from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockRuntimeGuardrailRegexFilter(BaseModel):
    name: StrictStr | None = None
    match: StrictStr | None = None
    regex: StrictStr | None = None
    action: StrictStr | None = None
    detected: StrictBool | None = None
