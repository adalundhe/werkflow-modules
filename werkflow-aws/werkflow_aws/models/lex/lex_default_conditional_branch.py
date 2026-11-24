from __future__ import annotations
from pydantic import BaseModel
from .lex_dialog_state import LexDialogState
from .lex_response_specification import LexResponseSpecification


class LexDefaultConditionalBranch(BaseModel):
    nextStep: LexDialogState | None = None
    response: LexResponseSpecification | None = None
