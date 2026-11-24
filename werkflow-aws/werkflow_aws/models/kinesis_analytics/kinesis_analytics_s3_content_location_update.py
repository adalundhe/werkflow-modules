from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsS3ContentLocationUpdate(BaseModel):
    BucketARNUpdate: StrictStr | None = None
    FileKeyUpdate: StrictStr | None = None
    ObjectVersionUpdate: StrictStr | None = None
