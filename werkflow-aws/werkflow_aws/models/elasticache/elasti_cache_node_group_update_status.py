from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_node_group_member_update_status import ElastiCacheNodeGroupMemberUpdateStatus


class ElastiCacheNodeGroupUpdateStatus(BaseModel):
    NodeGroupId: StrictStr | None = None
    NodeGroupMemberUpdateStatus: list[ElastiCacheNodeGroupMemberUpdateStatus] | None = None
