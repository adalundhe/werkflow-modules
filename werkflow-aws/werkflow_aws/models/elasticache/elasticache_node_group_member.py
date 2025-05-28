from pydantic import BaseModel, StrictStr
from .elasticache_endpoint import ElasticacheEndpoint


class ElasticacheNodeGroupMember(BaseModel):
    CacheClusterId: StrictStr
    CacheNodeId: StrictStr
    ReadEndpoint: ElasticacheEndpoint
    PreferredAvailabilityZone: StrictStr
    PreferredOutpostArn: StrictStr
    CurrentRole: StrictStr