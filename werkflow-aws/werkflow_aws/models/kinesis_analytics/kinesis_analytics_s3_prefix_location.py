from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsS3PrefixLocation(BaseModel):
    BucketARN: StrictStr | None = None
    KeyPrefix: StrictStr | None = None
