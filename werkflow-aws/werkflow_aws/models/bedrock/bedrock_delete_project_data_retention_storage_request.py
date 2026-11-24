from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class BedrockDeleteProjectDataRetentionStorageRequest(BaseModel):
    projectIdentifier: StrictStr
    modelProvider: Literal['anthropic', 'openai']
