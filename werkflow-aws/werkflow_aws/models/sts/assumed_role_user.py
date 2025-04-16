from pydantic import BaseModel, StrictStr


class AssumedRoledUser(BaseModel):
    AssumedRoleId: StrictStr
    Arn: StrictStr