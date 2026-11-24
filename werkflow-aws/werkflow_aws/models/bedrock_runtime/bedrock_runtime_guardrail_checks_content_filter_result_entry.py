from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BedrockRuntimeGuardrailChecksContentFilterResultEntry(BaseModel):
    category: StrictStr | None = None
    severityScore: StrictFloat | StrictInt | None = None
