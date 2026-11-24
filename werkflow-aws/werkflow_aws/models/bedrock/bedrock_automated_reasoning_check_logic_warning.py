from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_automated_reasoning_logic_statement import BedrockAutomatedReasoningLogicStatement


class BedrockAutomatedReasoningCheckLogicWarning(BaseModel):
    type: StrictStr | None = None
    premises: list[BedrockAutomatedReasoningLogicStatement] | None = None
    claims: list[BedrockAutomatedReasoningLogicStatement] | None = None
