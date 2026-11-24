from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_mlflow_config import SageMakerAIMlflowConfig


class SageMakerAIBenchmarkOutputConfig(BaseModel):
    S3OutputLocation: StrictStr
    MlflowConfig: SageMakerAIMlflowConfig | None = None
