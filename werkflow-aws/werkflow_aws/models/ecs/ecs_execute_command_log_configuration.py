from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECSExecuteCommandLogConfiguration(BaseModel):
    cloudWatchLogGroupName: StrictStr | None = None
    cloudWatchEncryptionEnabled: StrictBool | None = None
    s3BucketName: StrictStr | None = None
    s3EncryptionEnabled: StrictBool | None = None
    s3KeyPrefix: StrictStr | None = None
