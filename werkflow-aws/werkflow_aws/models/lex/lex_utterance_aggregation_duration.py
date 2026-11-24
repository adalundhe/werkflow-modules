from __future__ import annotations
from pydantic import BaseModel
from .lex_relative_aggregation_duration import LexRelativeAggregationDuration


class LexUtteranceAggregationDuration(BaseModel):
    relativeAggregationDuration: LexRelativeAggregationDuration | None = None
