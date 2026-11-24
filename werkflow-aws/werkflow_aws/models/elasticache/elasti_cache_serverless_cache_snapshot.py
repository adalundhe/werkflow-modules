from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .elasti_cache_serverless_cache_configuration import ElastiCacheServerlessCacheConfiguration


class ElastiCacheServerlessCacheSnapshot(BaseModel):
    ServerlessCacheSnapshotName: StrictStr | None = None
    ARN: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    SnapshotType: StrictStr | None = None
    Status: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    ExpiryTime: datetime.datetime | StrictStr | None = None
    BytesUsedForCache: StrictStr | None = None
    ServerlessCacheConfiguration: ElastiCacheServerlessCacheConfiguration | None = None
