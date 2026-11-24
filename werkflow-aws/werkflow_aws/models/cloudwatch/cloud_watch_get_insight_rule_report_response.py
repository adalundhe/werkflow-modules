from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .cloud_watch_insight_rule_contributor import CloudWatchInsightRuleContributor
from .cloud_watch_insight_rule_metric_datapoint import CloudWatchInsightRuleMetricDatapoint


class CloudWatchGetInsightRuleReportResponse(BaseModel):
    KeyLabels: list[StrictStr] | None = None
    AggregationStatistic: StrictStr | None = None
    AggregateValue: StrictFloat | StrictInt | None = None
    ApproximateUniqueCount: StrictInt | None = None
    Contributors: list[CloudWatchInsightRuleContributor] | None = None
    MetricDatapoints: list[CloudWatchInsightRuleMetricDatapoint] | None = None
    ResponseMetadata: dict[str, Any] | None = None
