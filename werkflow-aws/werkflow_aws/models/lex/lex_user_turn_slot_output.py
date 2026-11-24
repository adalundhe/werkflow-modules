from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexUserTurnSlotOutput(BaseModel):
    value: StrictStr | None = None
    values: list[LexUserTurnSlotOutput] | None = None
    subSlots: dict[StrictStr, LexUserTurnSlotOutput] | None = None
