from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockGuardrailConfiguration(BaseModel):
    guardrailId: StrictStr | None = None
    guardrailVersion: StrictStr | None = None
