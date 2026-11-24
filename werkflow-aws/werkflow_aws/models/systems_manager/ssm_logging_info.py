from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMLoggingInfo(BaseModel):
    S3BucketName: StrictStr | None = None
    S3KeyPrefix: StrictStr | None = None
    S3Region: StrictStr | None = None
