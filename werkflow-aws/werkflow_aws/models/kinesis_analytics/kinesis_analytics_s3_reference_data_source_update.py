from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsS3ReferenceDataSourceUpdate(BaseModel):
    BucketARNUpdate: StrictStr | None = None
    FileKeyUpdate: StrictStr | None = None
