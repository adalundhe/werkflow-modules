from pydantic import BaseModel, StrictStr


class AssumedRoleUser(BaseModel):
    AssumedRoleId: StrictStr
    Arn: StrictStr