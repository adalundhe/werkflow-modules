from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheRevokeCacheSecurityGroupIngressRequest(BaseModel):
    CacheSecurityGroupName: StrictStr
    EC2SecurityGroupName: StrictStr
    EC2SecurityGroupOwnerId: StrictStr
