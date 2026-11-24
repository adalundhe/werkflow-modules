from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_analytics_session_filter import LexAnalyticsSessionFilter
from .lex_session_data_sort_by import LexSessionDataSortBy


class LexListSessionAnalyticsDataRequest(BaseModel):
    botId: StrictStr
    startDateTime: datetime.datetime | StrictStr
    endDateTime: datetime.datetime | StrictStr
    sortBy: LexSessionDataSortBy | None = None
    filters: list[LexAnalyticsSessionFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
