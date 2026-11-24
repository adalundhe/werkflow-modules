from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTrainingJobStepMetadata(BaseModel):
    Arn: StrictStr | None = None
