from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_slot_value_override import LexSlotValueOverride


class LexIntentOverride(BaseModel):
    name: StrictStr | None = None
    slots: dict[StrictStr, LexSlotValueOverride] | None = None
