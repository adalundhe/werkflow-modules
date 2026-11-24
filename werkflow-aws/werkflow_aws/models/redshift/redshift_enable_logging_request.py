from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class RedshiftEnableLoggingRequest(BaseModel):
    ClusterIdentifier: StrictStr
    BucketName: StrictStr | None = None
    S3KeyPrefix: StrictStr | None = None
    LogDestinationType: Literal['s3', 'cloudwatch', 's3table'] | None = None
    LogExports: list[StrictStr] | None = None
    S3TableKmsKeyId: StrictStr | None = None
    S3TableGranularity: StrictStr | None = None
