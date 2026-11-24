from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lex_execution_error_details import LexExecutionErrorDetails


class LexAgentTurnResult(BaseModel):
    expectedAgentPrompt: StrictStr | None = None
    actualAgentPrompt: StrictStr | None = None
    errorDetails: LexExecutionErrorDetails | None = None
    actualElicitedSlot: StrictStr | None = None
    actualIntent: StrictStr | None = None
