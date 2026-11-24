from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BedrockRuntimeGuardrailChecksPromptAttackResultEntry(BaseModel):
    category: StrictStr | None = None
    severityScore: StrictFloat | StrictInt | None = None
