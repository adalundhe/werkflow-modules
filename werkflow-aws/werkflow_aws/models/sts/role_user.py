from pydantic import BaseModel, StrictStr


class RoleUser(BaseModel):
    AssumedRoleId: StrictStr
    Arn: StrictStr