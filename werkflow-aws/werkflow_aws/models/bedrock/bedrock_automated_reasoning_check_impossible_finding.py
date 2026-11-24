from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_reasoning_check_logic_warning import BedrockAutomatedReasoningCheckLogicWarning
from .bedrock_automated_reasoning_check_rule import BedrockAutomatedReasoningCheckRule
from .bedrock_automated_reasoning_check_translation import BedrockAutomatedReasoningCheckTranslation


class BedrockAutomatedReasoningCheckImpossibleFinding(BaseModel):
    translation: BedrockAutomatedReasoningCheckTranslation | None = None
    contradictingRules: list[BedrockAutomatedReasoningCheckRule] | None = None
    logicWarning: BedrockAutomatedReasoningCheckLogicWarning | None = None
