from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_analytics_bin_by_specification import LexAnalyticsBinBySpecification
from .lex_analytics_intent_filter import LexAnalyticsIntentFilter
from .lex_analytics_intent_group_by_specification import LexAnalyticsIntentGroupBySpecification
from .lex_analytics_intent_metric import LexAnalyticsIntentMetric


class LexListIntentMetricsRequest(BaseModel):
    botId: StrictStr
    startDateTime: datetime.datetime | StrictStr
    endDateTime: datetime.datetime | StrictStr
    metrics: list[LexAnalyticsIntentMetric]
    binBy: list[LexAnalyticsBinBySpecification] | None = None
    groupBy: list[LexAnalyticsIntentGroupBySpecification] | None = None
    filters: list[LexAnalyticsIntentFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
