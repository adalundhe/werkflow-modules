from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .elasti_cache_global_node_group import ElastiCacheGlobalNodeGroup
from .elasti_cache_global_replication_group_member import ElastiCacheGlobalReplicationGroupMember


class ElastiCacheGlobalReplicationGroup(BaseModel):
    GlobalReplicationGroupId: StrictStr | None = None
    GlobalReplicationGroupDescription: StrictStr | None = None
    Status: StrictStr | None = None
    CacheNodeType: StrictStr | None = None
    Engine: StrictStr | None = None
    EngineVersion: StrictStr | None = None
    Members: list[ElastiCacheGlobalReplicationGroupMember] | None = None
    ClusterEnabled: StrictBool | None = None
    GlobalNodeGroups: list[ElastiCacheGlobalNodeGroup] | None = None
    AuthTokenEnabled: StrictBool | None = None
    TransitEncryptionEnabled: StrictBool | None = None
    AtRestEncryptionEnabled: StrictBool | None = None
    ARN: StrictStr | None = None
