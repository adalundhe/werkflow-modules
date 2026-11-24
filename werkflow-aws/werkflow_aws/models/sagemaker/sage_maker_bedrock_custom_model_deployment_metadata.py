from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerBedrockCustomModelDeploymentMetadata(BaseModel):
    Arn: StrictStr | None = None
