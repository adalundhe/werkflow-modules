from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class BedrockGetAccountDataRetentionStorageRequest(BaseModel):
    modelProvider: Literal['anthropic', 'openai']
