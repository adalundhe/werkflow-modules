from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lex_input_context import LexInputContext
from .lex_output_context import LexOutputContext


class LexIntentSummary(BaseModel):
    intentId: StrictStr | None = None
    intentName: StrictStr | None = None
    intentDisplayName: StrictStr | None = None
    description: StrictStr | None = None
    parentIntentSignature: StrictStr | None = None
    inputContexts: list[LexInputContext] | None = None
    outputContexts: list[LexOutputContext] | None = None
    lastUpdatedDateTime: datetime.datetime | StrictStr | None = None
