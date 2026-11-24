from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAIModelSourceS3(BaseModel):
    S3Uri: StrictStr | None = None
