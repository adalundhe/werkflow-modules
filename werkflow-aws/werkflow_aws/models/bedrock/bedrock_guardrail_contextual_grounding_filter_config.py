from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt


class BedrockGuardrailContextualGroundingFilterConfig(BaseModel):
    type: Literal['GROUNDING', 'RELEVANCE']
    threshold: StrictFloat | StrictInt
    action: Literal['BLOCK', 'NONE'] | None = None
    enabled: StrictBool | None = None
