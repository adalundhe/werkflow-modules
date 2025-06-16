import datetime
from pydantic import (
    BaseModel,
    StrictStr,
)
from .organizations_joined_method import AWSJoinedMethod
from .organizations_account_status import AWSAccountStatus

class OrganizationsAccount(BaseModel):
    Id: StrictStr
    Arn: StrictStr
    Email: StrictStr
    Name: StrictStr
    Status: AWSAccountStatus
    JoinedMethod: AWSJoinedMethod
    JoinedTimestamp: datetime.datetime
