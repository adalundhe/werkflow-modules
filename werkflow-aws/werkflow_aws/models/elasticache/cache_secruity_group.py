from pydantic import BaseModel, StrictStr


class CacheSecurityGroup(BaseModel):
    CacheSecurityGroupName: StrictStr
    Status: StrictStr