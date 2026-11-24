from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAIWorkloadS3DataSource(BaseModel):
    S3Uri: StrictStr | None = None
