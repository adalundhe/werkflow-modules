from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_analytics_session_result import LexAnalyticsSessionResult


class LexListSessionMetricsResponse(BaseModel):
    botId: StrictStr | None = None
    results: list[LexAnalyticsSessionResult] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
