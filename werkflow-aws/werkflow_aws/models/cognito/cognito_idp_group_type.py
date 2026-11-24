from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class CognitoIDPGroupType(BaseModel):
    GroupName: StrictStr | None = None
    UserPoolId: StrictStr | None = None
    Description: StrictStr | None = None
    RoleArn: StrictStr | None = None
    Precedence: StrictInt | None = None
    LastModifiedDate: datetime.datetime | StrictStr | None = None
    CreationDate: datetime.datetime | StrictStr | None = None
