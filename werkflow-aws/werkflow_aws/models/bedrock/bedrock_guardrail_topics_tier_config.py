from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class BedrockGuardrailTopicsTierConfig(BaseModel):
    tierName: Literal['CLASSIC', 'STANDARD']
