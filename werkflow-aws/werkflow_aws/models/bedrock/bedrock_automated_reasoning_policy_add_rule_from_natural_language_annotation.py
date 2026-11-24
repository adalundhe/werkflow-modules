from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockAutomatedReasoningPolicyAddRuleFromNaturalLanguageAnnotation(BaseModel):
    naturalLanguage: StrictStr | None = None
