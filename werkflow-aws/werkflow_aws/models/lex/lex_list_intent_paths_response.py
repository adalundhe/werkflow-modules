from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lex_analytics_intent_node_summary import LexAnalyticsIntentNodeSummary


class LexListIntentPathsResponse(BaseModel):
    nodeSummaries: list[LexAnalyticsIntentNodeSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
