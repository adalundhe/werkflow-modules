from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsS3BucketLoggingConfiguration(BaseModel):
    DestinationBucketName: StrictStr | None = None
    LogFilePrefix: StrictStr | None = None
