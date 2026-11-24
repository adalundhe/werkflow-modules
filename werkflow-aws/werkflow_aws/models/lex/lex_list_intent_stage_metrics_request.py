from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .lex_analytics_bin_by_specification import LexAnalyticsBinBySpecification
from .lex_analytics_intent_stage_filter import LexAnalyticsIntentStageFilter
from .lex_analytics_intent_stage_group_by_specification import LexAnalyticsIntentStageGroupBySpecification
from .lex_analytics_intent_stage_metric import LexAnalyticsIntentStageMetric


class LexListIntentStageMetricsRequest(BaseModel):
    botId: StrictStr
    startDateTime: datetime.datetime | StrictStr
    endDateTime: datetime.datetime | StrictStr
    metrics: list[LexAnalyticsIntentStageMetric]
    binBy: list[LexAnalyticsBinBySpecification] | None = None
    groupBy: list[LexAnalyticsIntentStageGroupBySpecification] | None = None
    filters: list[LexAnalyticsIntentStageFilter] | None = None
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
