from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_runtime_hint_value import LexRuntimeHintValue


class LexRuntimeHintDetails(BaseModel):
    runtimeHintValues: list[LexRuntimeHintValue] | None = None
    subSlotHints: dict[StrictStr, LexRuntimeHintDetails] | None = None
