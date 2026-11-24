from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSNeptuneSettings(BaseModel):
    ServiceAccessRoleArn: StrictStr | None = None
    S3BucketName: StrictStr | None = None
    S3BucketFolder: StrictStr | None = None
    ErrorRetryDuration: StrictInt | None = None
    MaxFileSize: StrictInt | None = None
    MaxRetryCount: StrictInt | None = None
    IamAuthEnabled: StrictBool | None = None
