from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_metrics_source import SageMakerMetricsSource


class SageMakerDriftCheckModelDataQuality(BaseModel):
    Statistics: SageMakerMetricsSource | None = None
    Constraints: SageMakerMetricsSource | None = None
