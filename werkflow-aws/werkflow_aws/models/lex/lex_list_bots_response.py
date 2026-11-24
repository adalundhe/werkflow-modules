from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_summary import LexBotSummary


class LexListBotsResponse(BaseModel):
    botSummaries: list[LexBotSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
