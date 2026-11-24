from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_endpoint import ElastiCacheEndpoint


class ElastiCacheMigrationSummary(BaseModel):
    Status: StrictStr | None = None
    MigrationEndpoint: ElastiCacheEndpoint | None = None
    CutoverMode: StrictStr | None = None
