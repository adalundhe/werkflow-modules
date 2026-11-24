from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_s3_files_config import LambdaS3FilesConfig


class LambdaFileSystemConfig(BaseModel):
    Arn: StrictStr
    LocalMountPath: StrictStr
    S3FilesConfig: LambdaS3FilesConfig | None = None
