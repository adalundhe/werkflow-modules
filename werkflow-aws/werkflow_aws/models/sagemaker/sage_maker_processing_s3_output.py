from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_processing_s3_upload_mode import SageMakerProcessingS3UploadMode


class SageMakerProcessingS3Output(BaseModel):
    S3Uri: StrictStr | None = None
    LocalPath: StrictStr | None = None
    S3UploadMode: SageMakerProcessingS3UploadMode | None = None
