from __future__ import annotations
from pydantic import BaseModel
from .lex_sub_slot_type_composition import LexSubSlotTypeComposition


class LexCompositeSlotTypeSetting(BaseModel):
    subSlots: list[LexSubSlotTypeComposition] | None = None
