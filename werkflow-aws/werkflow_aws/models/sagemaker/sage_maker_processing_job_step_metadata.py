from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerProcessingJobStepMetadata(BaseModel):
    Arn: StrictStr | None = None
