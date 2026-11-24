from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_built_in_intent_summary import LexBuiltInIntentSummary


class LexListBuiltInIntentsResponse(BaseModel):
    builtInIntentSummaries: list[LexBuiltInIntentSummary] | None = None
    nextToken: StrictStr | None = None
    localeId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
