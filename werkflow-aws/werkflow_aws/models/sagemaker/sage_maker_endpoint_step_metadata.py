from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEndpointStepMetadata(BaseModel):
    Arn: StrictStr | None = None
