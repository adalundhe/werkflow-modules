from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class BedrockCreateGuardrailVersionResponse(BaseModel):
    guardrailId: StrictStr | None = None
    version: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
