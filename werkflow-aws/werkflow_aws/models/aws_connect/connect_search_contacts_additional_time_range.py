from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .connect_search_contacts_additional_time_range_criteria import ConnectSearchContactsAdditionalTimeRangeCriteria


class ConnectSearchContactsAdditionalTimeRange(BaseModel):
    Criteria: list[ConnectSearchContactsAdditionalTimeRangeCriteria]
    MatchType: Literal['MATCH_ALL', 'MATCH_ANY', 'MATCH_EXACT', 'MATCH_NONE']
