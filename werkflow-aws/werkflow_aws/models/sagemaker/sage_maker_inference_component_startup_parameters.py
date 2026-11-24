from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SageMakerInferenceComponentStartupParameters(BaseModel):
    ModelDataDownloadTimeoutInSeconds: StrictInt | None = None
    ContainerStartupHealthCheckTimeoutInSeconds: StrictInt | None = None
