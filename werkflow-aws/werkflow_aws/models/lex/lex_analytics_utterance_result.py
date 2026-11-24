from __future__ import annotations
from pydantic import BaseModel
from .lex_analytics_bin_key import LexAnalyticsBinKey
from .lex_analytics_utterance_attribute_result import LexAnalyticsUtteranceAttributeResult
from .lex_analytics_utterance_group_by_key import LexAnalyticsUtteranceGroupByKey
from .lex_analytics_utterance_metric_result import LexAnalyticsUtteranceMetricResult


class LexAnalyticsUtteranceResult(BaseModel):
    binKeys: list[LexAnalyticsBinKey] | None = None
    groupByKeys: list[LexAnalyticsUtteranceGroupByKey] | None = None
    metricsResults: list[LexAnalyticsUtteranceMetricResult] | None = None
    attributeResults: list[LexAnalyticsUtteranceAttributeResult] | None = None
