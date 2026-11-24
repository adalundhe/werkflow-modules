from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_bot_analyzer_history_summary import LexBotAnalyzerHistorySummary


class LexListBotAnalyzerHistoryResponse(BaseModel):
    botId: StrictStr | None = None
    localeId: StrictStr | None = None
    botVersion: StrictStr | None = None
    botAnalyzerHistoryList: list[LexBotAnalyzerHistorySummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
