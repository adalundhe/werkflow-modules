from pydantic import BaseModel, StrictStr


class ElasticacheCacheSecurityGroup(BaseModel):
    CacheSecurityGroupName: StrictStr
    Status: StrictStr