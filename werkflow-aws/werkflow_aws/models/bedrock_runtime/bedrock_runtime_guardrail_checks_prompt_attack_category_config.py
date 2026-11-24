from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class BedrockRuntimeGuardrailChecksPromptAttackCategoryConfig(BaseModel):
    category: Literal['JAILBREAK', 'PROMPT_INJECTION', 'PROMPT_LEAKAGE']
