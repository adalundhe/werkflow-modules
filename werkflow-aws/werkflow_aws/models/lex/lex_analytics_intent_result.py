from __future__ import annotations
from pydantic import BaseModel
from .lex_analytics_bin_key import LexAnalyticsBinKey
from .lex_analytics_intent_group_by_key import LexAnalyticsIntentGroupByKey
from .lex_analytics_intent_metric_result import LexAnalyticsIntentMetricResult


class LexAnalyticsIntentResult(BaseModel):
    binKeys: list[LexAnalyticsBinKey] | None = None
    groupByKeys: list[LexAnalyticsIntentGroupByKey] | None = None
    metricsResults: list[LexAnalyticsIntentMetricResult] | None = None
