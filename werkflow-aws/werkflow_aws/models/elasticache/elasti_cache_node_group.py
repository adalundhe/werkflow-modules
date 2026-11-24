from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_endpoint import ElastiCacheEndpoint
from .elasti_cache_node_group_member import ElastiCacheNodeGroupMember


class ElastiCacheNodeGroup(BaseModel):
    NodeGroupId: StrictStr | None = None
    Status: StrictStr | None = None
    PrimaryEndpoint: ElastiCacheEndpoint | None = None
    ReaderEndpoint: ElastiCacheEndpoint | None = None
    Slots: StrictStr | None = None
    NodeGroupMembers: list[ElastiCacheNodeGroupMember] | None = None
