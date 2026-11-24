from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_analytics_bin_by_specification import LexAnalyticsBinBySpecification
from .lex_analytics_session_filter import LexAnalyticsSessionFilter
from .lex_analytics_session_group_by_specification import LexAnalyticsSessionGroupBySpecification
from .lex_analytics_session_metric import LexAnalyticsSessionMetric


class LexListSessionMetricsRequest(BaseModel):
    botId: StrictStr
    startDateTime: datetime.datetime | StrictStr
    endDateTime: datetime.datetime | StrictStr
    metrics: list[LexAnalyticsSessionMetric]
    binBy: list[LexAnalyticsBinBySpecification] | None = None
    groupBy: list[LexAnalyticsSessionGroupBySpecification] | None = None
    filters: list[LexAnalyticsSessionFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
