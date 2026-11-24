from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_searchable_segment_attributes_criteria import ConnectSearchableSegmentAttributesCriteria


class ConnectSearchableSegmentAttributes(BaseModel):
    Criteria: list[ConnectSearchableSegmentAttributesCriteria]
    MatchType: Literal['MATCH_ALL', 'MATCH_ANY', 'MATCH_EXACT', 'MATCH_NONE'] | None = None
