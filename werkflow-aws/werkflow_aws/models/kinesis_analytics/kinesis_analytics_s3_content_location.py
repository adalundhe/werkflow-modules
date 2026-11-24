from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsS3ContentLocation(BaseModel):
    BucketARN: StrictStr | None = None
    FileKey: StrictStr | None = None
    ObjectVersion: StrictStr | None = None
