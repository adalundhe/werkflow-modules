from __future__ import annotations
from pydantic import BaseModel
from .lex_analytics_bin_key import LexAnalyticsBinKey
from .lex_analytics_intent_stage_group_by_key import LexAnalyticsIntentStageGroupByKey
from .lex_analytics_intent_stage_metric_result import LexAnalyticsIntentStageMetricResult


class LexAnalyticsIntentStageResult(BaseModel):
    binKeys: list[LexAnalyticsBinKey] | None = None
    groupByKeys: list[LexAnalyticsIntentStageGroupByKey] | None = None
    metricsResults: list[LexAnalyticsIntentStageMetricResult] | None = None
