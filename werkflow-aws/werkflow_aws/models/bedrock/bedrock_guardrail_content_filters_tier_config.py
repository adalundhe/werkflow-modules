from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class BedrockGuardrailContentFiltersTierConfig(BaseModel):
    tierName: Literal['CLASSIC', 'STANDARD']
