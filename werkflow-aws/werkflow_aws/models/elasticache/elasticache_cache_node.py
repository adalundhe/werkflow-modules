import datetime
from pydantic import BaseModel, StrictStr
from .elasticache_endpoint import ElasticacheEndpoint


class ElasticacheCacheNode(BaseModel):
    CacheNodeId: StrictStr
    CacheNodeStatus: StrictStr
    CacheNodeCreateTime: datetime.datetime
    Endpoint: ElasticacheEndpoint
    ParameterGroupStatus: StrictStr
    SourceCacheNodeId: StrictStr
    CustomerAvailabilityZone: StrictStr
    CustomerOutpostArn: StrictStr
