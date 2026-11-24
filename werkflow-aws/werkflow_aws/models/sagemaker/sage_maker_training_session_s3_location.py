from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerTrainingSessionS3Location(BaseModel):
    Path: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
