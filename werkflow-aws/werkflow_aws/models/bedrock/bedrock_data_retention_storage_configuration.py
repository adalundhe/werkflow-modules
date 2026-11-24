from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockDataRetentionStorageConfiguration(BaseModel):
    kmsKeyArn: StrictStr | None = None
    s3BucketArn: StrictStr | None = None
    s3BucketOwner: StrictStr | None = None
