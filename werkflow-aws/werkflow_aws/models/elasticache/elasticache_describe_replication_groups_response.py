from pydantic import BaseModel, StrictStr
from .elasticache_replication_group import ElasticacheReplicationGroup


class ElasticacheDescribeReplicationGroupsResponse(BaseModel):
    Marker: StrictStr
    ReplicationGroups: list[ElasticacheReplicationGroup]

