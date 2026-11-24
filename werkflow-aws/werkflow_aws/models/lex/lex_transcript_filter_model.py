from __future__ import annotations
from pydantic import BaseModel
from .lex_date_range_filter import LexDateRangeFilter


class LexTranscriptFilterModel(BaseModel):
    dateRangeFilter: LexDateRangeFilter | None = None
