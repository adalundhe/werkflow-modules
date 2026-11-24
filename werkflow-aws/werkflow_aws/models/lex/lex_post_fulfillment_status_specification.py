from __future__ import annotations
from pydantic import BaseModel
from .lex_conditional_specification import LexConditionalSpecification
from .lex_dialog_state import LexDialogState
from .lex_response_specification import LexResponseSpecification


class LexPostFulfillmentStatusSpecification(BaseModel):
    successResponse: LexResponseSpecification | None = None
    failureResponse: LexResponseSpecification | None = None
    timeoutResponse: LexResponseSpecification | None = None
    successNextStep: LexDialogState | None = None
    successConditional: LexConditionalSpecification | None = None
    failureNextStep: LexDialogState | None = None
    failureConditional: LexConditionalSpecification | None = None
    timeoutNextStep: LexDialogState | None = None
    timeoutConditional: LexConditionalSpecification | None = None
