from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BedrockAutomatedReasoningPolicyAnnotatedLine(BaseModel):
    lineNumber: StrictInt | None = None
    lineText: StrictStr | None = None
