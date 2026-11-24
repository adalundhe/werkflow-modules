from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_intent_summary import LexIntentSummary


class LexListIntentsResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    localeId: StrictStr | None = None
    intentSummaries: list[LexIntentSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
