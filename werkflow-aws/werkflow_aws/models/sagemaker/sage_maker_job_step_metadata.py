from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerJobStepMetadata(BaseModel):
    Arn: StrictStr | None = None
