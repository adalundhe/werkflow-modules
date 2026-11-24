from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyBedrockGuardrailResource(BaseModel):
    Version: StrictStr | None = None
    GuardrailAction: StrictStr | None = None
    GuardrailSource: StrictStr | None = None
