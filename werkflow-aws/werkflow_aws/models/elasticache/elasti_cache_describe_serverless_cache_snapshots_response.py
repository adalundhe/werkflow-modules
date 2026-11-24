from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .elasti_cache_serverless_cache_snapshot import ElastiCacheServerlessCacheSnapshot


class ElastiCacheDescribeServerlessCacheSnapshotsResponse(BaseModel):
    NextToken: StrictStr | None = None
    ServerlessCacheSnapshots: list[ElastiCacheServerlessCacheSnapshot] | None = None
    ResponseMetadata: dict[str, Any] | None = None
