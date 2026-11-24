from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_specifications import LexSpecifications


class LexSubSlotSetting(BaseModel):
    expression: StrictStr | None = None
    slotSpecifications: dict[StrictStr, LexSpecifications] | None = None
