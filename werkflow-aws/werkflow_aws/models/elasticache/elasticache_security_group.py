from pydantic import BaseModel, StrictStr


class ElasticacheSecurityGroup(BaseModel):
    SecurityGroupId: StrictStr
    Status: StrictStr