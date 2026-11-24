from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_locale_summary import LexBotLocaleSummary


class LexListBotLocalesResponse(BaseModel):
    botId: StrictStr | None = None
    botVersion: StrictStr | None = None
    nextToken: StrictStr | None = None
    botLocaleSummaries: list[LexBotLocaleSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
