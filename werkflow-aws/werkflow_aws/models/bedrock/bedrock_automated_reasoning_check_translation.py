from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .bedrock_automated_reasoning_check_input_text_reference import BedrockAutomatedReasoningCheckInputTextReference
from .bedrock_automated_reasoning_logic_statement import BedrockAutomatedReasoningLogicStatement


class BedrockAutomatedReasoningCheckTranslation(BaseModel):
    premises: list[BedrockAutomatedReasoningLogicStatement] | None = None
    claims: list[BedrockAutomatedReasoningLogicStatement] | None = None
    untranslatedPremises: list[BedrockAutomatedReasoningCheckInputTextReference] | None = None
    untranslatedClaims: list[BedrockAutomatedReasoningCheckInputTextReference] | None = None
    confidence: StrictFloat | StrictInt | None = None
