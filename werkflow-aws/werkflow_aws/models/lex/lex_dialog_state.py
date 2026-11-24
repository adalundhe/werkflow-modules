from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_dialog_action import LexDialogAction
from .lex_intent_override import LexIntentOverride


class LexDialogState(BaseModel):
    dialogAction: LexDialogAction | None = None
    intent: LexIntentOverride | None = None
    sessionAttributes: dict[StrictStr, StrictStr] | None = None
