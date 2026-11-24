from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningLogicStatement(BaseModel):
    logic: StrictStr | None = None
    naturalLanguage: StrictStr | None = None
