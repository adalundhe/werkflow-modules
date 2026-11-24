from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsSnapshotOperationS3PrefixLocation(BaseModel):
    BucketARN: StrictStr | None = None
    KeyPrefix: StrictStr | None = None
    ExportedPrefix: StrictStr | None = None
