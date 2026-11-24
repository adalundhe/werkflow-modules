from __future__ import annotations
from pydantic import BaseModel
from .lex_analytics_bin_key import LexAnalyticsBinKey
from .lex_analytics_session_group_by_key import LexAnalyticsSessionGroupByKey
from .lex_analytics_session_metric_result import LexAnalyticsSessionMetricResult


class LexAnalyticsSessionResult(BaseModel):
    binKeys: list[LexAnalyticsBinKey] | None = None
    groupByKeys: list[LexAnalyticsSessionGroupByKey] | None = None
    metricsResults: list[LexAnalyticsSessionMetricResult] | None = None
