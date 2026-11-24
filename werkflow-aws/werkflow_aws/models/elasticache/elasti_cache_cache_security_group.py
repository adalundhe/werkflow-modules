from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .elasti_cache_ec2_security_group import ElastiCacheEC2SecurityGroup


class ElastiCacheCacheSecurityGroup(BaseModel):
    OwnerId: StrictStr | None = None
    CacheSecurityGroupName: StrictStr | None = None
    Description: StrictStr | None = None
    EC2SecurityGroups: list[ElastiCacheEC2SecurityGroup] | None = None
    ARN: StrictStr | None = None
