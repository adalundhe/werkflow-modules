from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerMonitoringS3Output(BaseModel):
    S3Uri: StrictStr | None = None
    LocalPath: StrictStr | None = None
    S3UploadMode: StrictStr | None = None
