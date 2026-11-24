from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class BedrockRuntimeGuardrailTextBlock(BaseModel):
    text: StrictStr
    qualifiers: list[Literal['grounding_source', 'query', 'guard_content']] | None = None
