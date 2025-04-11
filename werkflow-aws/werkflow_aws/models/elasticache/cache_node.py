import datetime
from pydantic import BaseModel, StrictStr
from .endpoint import Endpoint


class CacheNode(BaseModel):
    CacheNodeId: StrictStr
    CacheNodeStatus: StrictStr
    CacheNodeCreateTime: datetime.datetime
    Endpoint: Endpoint
    ParameterGroupStatus: StrictStr
    SourceCacheNodeId: StrictStr
    CustomerAvailabilityZone: StrictStr
    CustomerOutpostArn: StrictStr
