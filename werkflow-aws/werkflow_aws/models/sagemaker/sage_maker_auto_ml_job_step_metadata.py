from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAutoMLJobStepMetadata(BaseModel):
    Arn: StrictStr | None = None
