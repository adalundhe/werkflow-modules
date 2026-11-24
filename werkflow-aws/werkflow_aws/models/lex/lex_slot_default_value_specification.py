from __future__ import annotations
from pydantic import BaseModel
from .lex_slot_default_value import LexSlotDefaultValue


class LexSlotDefaultValueSpecification(BaseModel):
    defaultValueList: list[LexSlotDefaultValue] | None = None
