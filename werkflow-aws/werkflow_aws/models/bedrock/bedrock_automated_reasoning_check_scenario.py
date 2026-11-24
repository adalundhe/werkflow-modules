from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_reasoning_logic_statement import BedrockAutomatedReasoningLogicStatement


class BedrockAutomatedReasoningCheckScenario(BaseModel):
    statements: list[BedrockAutomatedReasoningLogicStatement] | None = None
