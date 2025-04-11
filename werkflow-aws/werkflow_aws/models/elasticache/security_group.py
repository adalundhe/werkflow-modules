from pydantic import BaseModel, StrictStr


class SecurityGroup(BaseModel):
    SecurityGroupId: StrictStr
    Status: StrictStr