from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerS3FileSystemConfig(BaseModel):
    MountPath: StrictStr | None = None
    S3Uri: StrictStr | None = None
