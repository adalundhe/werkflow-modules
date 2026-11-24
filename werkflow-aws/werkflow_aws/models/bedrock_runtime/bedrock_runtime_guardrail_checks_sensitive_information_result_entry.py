from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class BedrockRuntimeGuardrailChecksSensitiveInformationResultEntry(BaseModel):
    type: StrictStr | None = None
    confidenceScore: StrictFloat | StrictInt | None = None
    beginOffset: StrictInt | None = None
    endOffset: StrictInt | None = None
    messageIndex: StrictInt | None = None
    contentIndex: StrictInt | None = None
