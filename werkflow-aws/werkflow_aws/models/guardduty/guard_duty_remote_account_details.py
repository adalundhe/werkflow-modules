from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GuardDutyRemoteAccountDetails(BaseModel):
    AccountId: StrictStr | None = None
    Affiliated: StrictBool | None = None
    AwsServiceName: StrictStr | None = None
