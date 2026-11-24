from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEdgeDeploymentConfig(BaseModel):
    FailureHandlingPolicy: StrictStr | None = None
