from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_data_quality_metric_values import GlueDataQualityMetricValues


class GlueMetricBasedObservation(BaseModel):
    MetricName: StrictStr | None = None
    StatisticId: StrictStr | None = None
    MetricValues: GlueDataQualityMetricValues | None = None
    NewRules: list[StrictStr] | None = None
