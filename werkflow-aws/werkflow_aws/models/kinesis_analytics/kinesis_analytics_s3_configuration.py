from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsS3Configuration(BaseModel):
    BucketARN: StrictStr
    FileKey: StrictStr
