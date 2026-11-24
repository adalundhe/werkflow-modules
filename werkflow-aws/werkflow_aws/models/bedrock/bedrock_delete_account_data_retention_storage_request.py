from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class BedrockDeleteAccountDataRetentionStorageRequest(BaseModel):
    modelProvider: Literal['anthropic', 'openai']
