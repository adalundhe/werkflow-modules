from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ElastiCacheAuthorizeCacheSecurityGroupIngressRequest(BaseModel):
    CacheSecurityGroupName: StrictStr
    EC2SecurityGroupName: StrictStr
    EC2SecurityGroupOwnerId: StrictStr
