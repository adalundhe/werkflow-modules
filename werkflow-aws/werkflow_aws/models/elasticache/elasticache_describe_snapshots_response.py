from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasticache_snapshot import ElasticacheSnapshot


class ElasticacheDescribeSnapshotsResponse(BaseModel):
    Marker: StrictStr | None = None
    Snapshots: list[ElasticacheSnapshot] | None = None
