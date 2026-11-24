from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_metrics_source import SageMakerMetricsSource


class SageMakerBias(BaseModel):
    Report: SageMakerMetricsSource | None = None
    PreTrainingReport: SageMakerMetricsSource | None = None
    PostTrainingReport: SageMakerMetricsSource | None = None
