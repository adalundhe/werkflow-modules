from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerS3StorageConfig(BaseModel):
    S3Uri: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    ResolvedOutputS3Uri: StrictStr | None = None
