from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_analytics_utterance_filter import LexAnalyticsUtteranceFilter
from .lex_utterance_data_sort_by import LexUtteranceDataSortBy


class LexListUtteranceAnalyticsDataRequest(BaseModel):
    botId: StrictStr
    startDateTime: datetime.datetime | StrictStr
    endDateTime: datetime.datetime | StrictStr
    sortBy: LexUtteranceDataSortBy | None = None
    filters: list[LexAnalyticsUtteranceFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
