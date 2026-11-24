from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .mwaa_metric_datum import MWAAMetricDatum


class MWAAPublishMetricsRequest(BaseModel):
    EnvironmentName: StrictStr
    MetricData: list[MWAAMetricDatum]
