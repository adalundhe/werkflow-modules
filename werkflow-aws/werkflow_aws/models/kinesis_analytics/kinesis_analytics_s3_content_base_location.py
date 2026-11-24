from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsS3ContentBaseLocation(BaseModel):
    BucketARN: StrictStr
    BasePath: StrictStr | None = None
