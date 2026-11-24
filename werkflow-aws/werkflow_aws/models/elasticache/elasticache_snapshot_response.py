from __future__ import annotations
from pydantic import BaseModel
from .elasticache_snapshot import ElasticacheSnapshot


class ElasticacheSnapshotResponse(BaseModel):
    Snapshot: ElasticacheSnapshot | None = None
