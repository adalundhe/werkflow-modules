from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_metric_based_observation import GlueMetricBasedObservation


class GlueDataQualityObservation(BaseModel):
    Description: StrictStr | None = None
    MetricBasedObservation: GlueMetricBasedObservation | None = None
