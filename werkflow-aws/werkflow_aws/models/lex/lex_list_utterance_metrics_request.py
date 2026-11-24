from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_analytics_bin_by_specification import LexAnalyticsBinBySpecification
from .lex_analytics_utterance_attribute import LexAnalyticsUtteranceAttribute
from .lex_analytics_utterance_filter import LexAnalyticsUtteranceFilter
from .lex_analytics_utterance_group_by_specification import LexAnalyticsUtteranceGroupBySpecification
from .lex_analytics_utterance_metric import LexAnalyticsUtteranceMetric


class LexListUtteranceMetricsRequest(BaseModel):
    botId: StrictStr
    startDateTime: datetime.datetime | StrictStr
    endDateTime: datetime.datetime | StrictStr
    metrics: list[LexAnalyticsUtteranceMetric]
    binBy: list[LexAnalyticsBinBySpecification] | None = None
    groupBy: list[LexAnalyticsUtteranceGroupBySpecification] | None = None
    attributes: list[LexAnalyticsUtteranceAttribute] | None = None
    filters: list[LexAnalyticsUtteranceFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
