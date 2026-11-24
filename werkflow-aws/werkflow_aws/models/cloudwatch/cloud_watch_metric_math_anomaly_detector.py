from __future__ import annotations
from pydantic import BaseModel
from .cloud_watch_metric_data_query_model import CloudWatchMetricDataQueryModel


class CloudWatchMetricMathAnomalyDetector(BaseModel):
    MetricDataQueries: list[CloudWatchMetricDataQueryModel] | None = None
