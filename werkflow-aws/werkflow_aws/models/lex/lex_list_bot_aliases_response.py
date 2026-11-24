from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_alias_summary import LexBotAliasSummary


class LexListBotAliasesResponse(BaseModel):
    botAliasSummaries: list[LexBotAliasSummary] | None = None
    nextToken: StrictStr | None = None
    botId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
