from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool


class BedrockGuardrailContentFilterConfig(BaseModel):
    type: Literal['SEXUAL', 'VIOLENCE', 'HATE', 'INSULTS', 'MISCONDUCT', 'PROMPT_ATTACK']
    inputStrength: Literal['NONE', 'LOW', 'MEDIUM', 'HIGH']
    outputStrength: Literal['NONE', 'LOW', 'MEDIUM', 'HIGH']
    inputModalities: list[Literal['TEXT', 'IMAGE']] | None = None
    outputModalities: list[Literal['TEXT', 'IMAGE']] | None = None
    inputAction: Literal['BLOCK', 'NONE'] | None = None
    outputAction: Literal['BLOCK', 'NONE'] | None = None
    inputEnabled: StrictBool | None = None
    outputEnabled: StrictBool | None = None
