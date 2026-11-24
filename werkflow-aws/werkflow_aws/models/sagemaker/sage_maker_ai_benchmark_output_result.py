from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_ai_cloud_watch_logs import SageMakerAICloudWatchLogs
from .sage_maker_ai_mlflow_config import SageMakerAIMlflowConfig


class SageMakerAIBenchmarkOutputResult(BaseModel):
    S3OutputLocation: StrictStr | None = None
    CloudWatchLogs: list[SageMakerAICloudWatchLogs] | None = None
    MlflowConfig: SageMakerAIMlflowConfig | None = None
