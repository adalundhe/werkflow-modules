from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .lex_response_specification import LexResponseSpecification
from .lex_still_waiting_response_specification import LexStillWaitingResponseSpecification


class LexWaitAndContinueSpecification(BaseModel):
    waitingResponse: LexResponseSpecification | None = None
    continueResponse: LexResponseSpecification | None = None
    stillWaitingResponse: LexStillWaitingResponseSpecification | None = None
    active: StrictBool | None = None
