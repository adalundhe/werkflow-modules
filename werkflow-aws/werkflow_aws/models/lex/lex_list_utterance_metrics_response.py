from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_analytics_utterance_result import LexAnalyticsUtteranceResult


class LexListUtteranceMetricsResponse(BaseModel):
    botId: StrictStr | None = None
    results: list[LexAnalyticsUtteranceResult] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
