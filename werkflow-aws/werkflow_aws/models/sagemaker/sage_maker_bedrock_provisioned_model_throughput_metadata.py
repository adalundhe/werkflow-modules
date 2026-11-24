from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerBedrockProvisionedModelThroughputMetadata(BaseModel):
    Arn: StrictStr | None = None
