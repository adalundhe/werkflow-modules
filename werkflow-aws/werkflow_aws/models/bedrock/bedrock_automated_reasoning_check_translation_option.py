from __future__ import annotations
from pydantic import BaseModel
from .bedrock_automated_reasoning_check_translation import BedrockAutomatedReasoningCheckTranslation


class BedrockAutomatedReasoningCheckTranslationOption(BaseModel):
    translations: list[BedrockAutomatedReasoningCheckTranslation] | None = None
