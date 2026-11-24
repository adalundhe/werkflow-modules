from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectClaimPhoneNumberRequest(BaseModel):
    PhoneNumber: StrictStr
    TargetArn: StrictStr | None = None
    InstanceId: StrictStr | None = None
    PhoneNumberDescription: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ClientToken: StrictStr | None = None
