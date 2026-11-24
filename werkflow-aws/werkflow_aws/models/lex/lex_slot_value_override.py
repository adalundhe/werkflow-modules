from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_slot_value import LexSlotValue


class LexSlotValueOverride(BaseModel):
    shape: StrictStr | None = None
    value: LexSlotValue | None = None
    values: list[LexSlotValueOverride] | None = None
