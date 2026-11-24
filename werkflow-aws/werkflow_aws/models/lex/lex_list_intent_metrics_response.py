from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_analytics_intent_result import LexAnalyticsIntentResult


class LexListIntentMetricsResponse(BaseModel):
    botId: StrictStr | None = None
    results: list[LexAnalyticsIntentResult] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
