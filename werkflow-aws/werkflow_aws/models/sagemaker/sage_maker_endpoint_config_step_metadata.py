from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerEndpointConfigStepMetadata(BaseModel):
    Arn: StrictStr | None = None
