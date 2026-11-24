from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdatePhoneNumberRequest(BaseModel):
    PhoneNumberId: StrictStr
    TargetArn: StrictStr | None = None
    InstanceId: StrictStr | None = None
    ClientToken: StrictStr | None = None
