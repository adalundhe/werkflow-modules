from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .msk_user_identity import MSKUserIdentity


class MSKVpcConnectionInfoServerless(BaseModel):
    CreationTime: datetime.datetime | StrictStr | None = None
    Owner: StrictStr | None = None
    UserIdentity: MSKUserIdentity | None = None
    VpcConnectionArn: StrictStr | None = None
