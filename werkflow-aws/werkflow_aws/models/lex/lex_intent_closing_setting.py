from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lex_conditional_specification import LexConditionalSpecification
from .lex_dialog_state import LexDialogState
from .lex_response_specification import LexResponseSpecification


class LexIntentClosingSetting(BaseModel):
    closingResponse: LexResponseSpecification | None = None
    active: StrictBool | None = None
    nextStep: LexDialogState | None = None
    conditional: LexConditionalSpecification | None = None
