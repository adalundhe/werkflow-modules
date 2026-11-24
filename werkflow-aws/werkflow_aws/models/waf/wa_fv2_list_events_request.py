from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_api_pattern_filter import WAFv2ApiPatternFilter
from .wa_fv2_event_filter import WAFv2EventFilter
from .wa_fv2_time_window import WAFv2TimeWindow


class WAFv2ListEventsRequest(BaseModel):
    Scope: Literal['CLOUDFRONT', 'REGIONAL']
    TimeWindow: WAFv2TimeWindow | None = None
    Filters: list[WAFv2EventFilter] | None = None
    ApiPatternFilters: list[WAFv2ApiPatternFilter] | None = None
    Limit: StrictInt | None = None
    NextMarker: StrictStr | None = None
    SortOrder: Literal['ASC', 'DESC'] | None = None
    SortBy: Literal['START_TIME', 'END_TIME', 'CONFIDENCE'] | None = None
    Include: list[Literal['TIMELINE']] | None = None
