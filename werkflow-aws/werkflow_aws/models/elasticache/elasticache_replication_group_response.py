from __future__ import annotations
from pydantic import BaseModel
from .elasticache_replication_group import ElasticacheReplicationGroup


class ElasticacheReplicationGroupResponse(BaseModel):
    ReplicationGroup: ElasticacheReplicationGroup | None = None
