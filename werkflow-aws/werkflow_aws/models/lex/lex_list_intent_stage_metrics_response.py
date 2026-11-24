from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lex_analytics_intent_stage_result import LexAnalyticsIntentStageResult


class LexListIntentStageMetricsResponse(BaseModel):
    botId: StrictStr | None = None
    results: list[LexAnalyticsIntentStageResult] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
