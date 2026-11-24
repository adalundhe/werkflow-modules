from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerProcessingS3OutputModel(BaseModel):
    S3Uri: StrictStr | None = None
    LocalPath: StrictStr | None = None
    S3UploadMode: StrictStr | None = None
