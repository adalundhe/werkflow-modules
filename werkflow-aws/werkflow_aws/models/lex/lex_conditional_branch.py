from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_condition import LexCondition
from .lex_dialog_state import LexDialogState
from .lex_response_specification import LexResponseSpecification


class LexConditionalBranch(BaseModel):
    name: StrictStr | None = None
    condition: LexCondition | None = None
    nextStep: LexDialogState | None = None
    response: LexResponseSpecification | None = None
