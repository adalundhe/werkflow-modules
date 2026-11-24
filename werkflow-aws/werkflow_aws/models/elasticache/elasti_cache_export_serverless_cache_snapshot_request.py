from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheExportServerlessCacheSnapshotRequest(BaseModel):
    ServerlessCacheSnapshotName: StrictStr
    S3BucketName: StrictStr
