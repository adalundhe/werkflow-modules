from __future__ import annotations
from pydantic import BaseModel
from .bedrock_validator import BedrockValidator


class BedrockValidationDataConfig(BaseModel):
    validators: list[BedrockValidator] | None = None
