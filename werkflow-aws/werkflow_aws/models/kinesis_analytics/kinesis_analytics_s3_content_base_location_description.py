from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsS3ContentBaseLocationDescription(BaseModel):
    BucketARN: StrictStr | None = None
    BasePath: StrictStr | None = None
