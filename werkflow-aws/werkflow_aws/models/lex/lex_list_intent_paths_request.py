from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lex_analytics_path_filter import LexAnalyticsPathFilter


class LexListIntentPathsRequest(BaseModel):
    botId: StrictStr
    startDateTime: datetime.datetime | StrictStr
    endDateTime: datetime.datetime | StrictStr
    intentPath: StrictStr
    filters: list[LexAnalyticsPathFilter] | None = None
