from __future__ import annotations
from pydantic import BaseModel, StrictBytes, StrictStr
from .lambda_s3_object_storage_mode import LambdaS3ObjectStorageMode


class LambdaFunctionCode(BaseModel):
    ZipFile: StrictBytes | None = None
    S3Bucket: StrictStr | None = None
    S3Key: StrictStr | None = None
    S3ObjectVersion: StrictStr | None = None
    S3ObjectStorageMode: LambdaS3ObjectStorageMode | None = None
    ImageUri: StrictStr | None = None
    SourceKMSKeyArn: StrictStr | None = None
