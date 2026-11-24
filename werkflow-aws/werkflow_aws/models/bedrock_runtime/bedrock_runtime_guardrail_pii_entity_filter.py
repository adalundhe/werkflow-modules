from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BedrockRuntimeGuardrailPiiEntityFilter(BaseModel):
    match: StrictStr | None = None
    type: StrictStr | None = None
    action: StrictStr | None = None
    detected: StrictBool | None = None
