from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_user_turn_slot_output import LexUserTurnSlotOutput


class LexUserTurnIntentOutput(BaseModel):
    name: StrictStr | None = None
    slots: dict[StrictStr, LexUserTurnSlotOutput] | None = None
