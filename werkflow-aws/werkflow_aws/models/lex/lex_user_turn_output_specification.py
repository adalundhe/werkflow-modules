from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_active_context import LexActiveContext
from .lex_user_turn_intent_output import LexUserTurnIntentOutput


class LexUserTurnOutputSpecification(BaseModel):
    intent: LexUserTurnIntentOutput | None = None
    activeContexts: list[LexActiveContext] | None = None
    transcript: StrictStr | None = None
