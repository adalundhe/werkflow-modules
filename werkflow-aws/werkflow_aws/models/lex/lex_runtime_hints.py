from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_runtime_hint_details import LexRuntimeHintDetails


class LexRuntimeHints(BaseModel):
    slotHints: dict[StrictStr, dict[StrictStr, LexRuntimeHintDetails]] | None = None
