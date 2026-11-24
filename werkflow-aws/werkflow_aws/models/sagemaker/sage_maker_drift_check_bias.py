from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_file_source import SageMakerFileSource
from .sage_maker_metrics_source import SageMakerMetricsSource


class SageMakerDriftCheckBias(BaseModel):
    ConfigFile: SageMakerFileSource | None = None
    PreTrainingConstraints: SageMakerMetricsSource | None = None
    PostTrainingConstraints: SageMakerMetricsSource | None = None
