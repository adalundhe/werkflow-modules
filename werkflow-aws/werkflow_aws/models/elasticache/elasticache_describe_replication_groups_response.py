from pydantic import BaseModel, StrictStr
from .elasticache_replication_group import ElasticacheReplicationGroup


class ElasticacheDescribeReplicationGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    ReplicationGroups: list[ElasticacheReplicationGroup] | None = None
