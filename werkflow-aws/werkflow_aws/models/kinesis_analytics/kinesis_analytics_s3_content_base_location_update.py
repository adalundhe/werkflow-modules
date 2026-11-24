from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsS3ContentBaseLocationUpdate(BaseModel):
    BucketARNUpdate: StrictStr | None = None
    BasePathUpdate: StrictStr | None = None
