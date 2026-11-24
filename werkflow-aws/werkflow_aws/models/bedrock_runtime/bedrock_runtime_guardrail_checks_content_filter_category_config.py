from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class BedrockRuntimeGuardrailChecksContentFilterCategoryConfig(BaseModel):
    category: Literal['VIOLENCE', 'HATE', 'SEXUAL', 'MISCONDUCT', 'INSULTS']
