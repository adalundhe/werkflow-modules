from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_reasoning_check_scenario import BedrockAutomatedReasoningCheckScenario
from .bedrock_automated_reasoning_check_translation_option import BedrockAutomatedReasoningCheckTranslationOption


class BedrockAutomatedReasoningCheckTranslationAmbiguousFinding(BaseModel):
    options: list[BedrockAutomatedReasoningCheckTranslationOption] | None = None
    differenceScenarios: list[BedrockAutomatedReasoningCheckScenario] | None = None
