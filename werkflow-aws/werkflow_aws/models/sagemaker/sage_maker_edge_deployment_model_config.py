from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEdgeDeploymentModelConfig(BaseModel):
    ModelHandle: StrictStr | None = None
    EdgePackagingJobName: StrictStr | None = None
