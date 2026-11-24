from __future__ import annotations
from pydantic import BaseModel
from .lex_conditional_specification import LexConditionalSpecification
from .lex_dialog_state import LexDialogState
from .lex_response_specification import LexResponseSpecification


class LexPostDialogCodeHookInvocationSpecification(BaseModel):
    successResponse: LexResponseSpecification | None = None
    successNextStep: LexDialogState | None = None
    successConditional: LexConditionalSpecification | None = None
    failureResponse: LexResponseSpecification | None = None
    failureNextStep: LexDialogState | None = None
    failureConditional: LexConditionalSpecification | None = None
    timeoutResponse: LexResponseSpecification | None = None
    timeoutNextStep: LexDialogState | None = None
    timeoutConditional: LexConditionalSpecification | None = None
