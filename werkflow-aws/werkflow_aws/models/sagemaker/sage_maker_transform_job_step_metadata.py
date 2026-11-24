from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTransformJobStepMetadata(BaseModel):
    Arn: StrictStr | None = None
