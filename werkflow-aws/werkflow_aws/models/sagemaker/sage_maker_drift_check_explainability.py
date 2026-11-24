from __future__ import annotations
from pydantic import BaseModel
from .sage_maker_file_source import SageMakerFileSource
from .sage_maker_metrics_source import SageMakerMetricsSource


class SageMakerDriftCheckExplainability(BaseModel):
    Constraints: SageMakerMetricsSource | None = None
    ConfigFile: SageMakerFileSource | None = None
