from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_version_summary import LexBotVersionSummary


class LexListBotVersionsResponse(BaseModel):
    botId: StrictStr | None = None
    botVersionSummaries: list[LexBotVersionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
