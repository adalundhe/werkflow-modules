from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictBytes, StrictStr
from .lambda_architecture import LambdaArchitecture
from .lambda_function_version_latest_published import LambdaFunctionVersionLatestPublished
from .lambda_s3_object_storage_mode import LambdaS3ObjectStorageMode


class LambdaUpdateFunctionCodeRequest(BaseModel):
    FunctionName: StrictStr
    ZipFile: StrictBytes | None = None
    S3Bucket: StrictStr | None = None
    S3Key: StrictStr | None = None
    S3ObjectVersion: StrictStr | None = None
    S3ObjectStorageMode: LambdaS3ObjectStorageMode | None = None
    ImageUri: StrictStr | None = None
    Architectures: list[LambdaArchitecture] | None = None
    Publish: StrictBool | None = None
    PublishTo: LambdaFunctionVersionLatestPublished | None = None
    DryRun: StrictBool | None = None
    RevisionId: StrictStr | None = None
    SourceKMSKeyArn: StrictStr | None = None
