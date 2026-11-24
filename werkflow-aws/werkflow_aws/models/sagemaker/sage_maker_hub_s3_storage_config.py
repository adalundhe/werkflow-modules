from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerHubS3StorageConfig(BaseModel):
    S3OutputPath: StrictStr | None = None
