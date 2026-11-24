from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class ConnectUserPhoneConfig(BaseModel):
    PhoneType: StrictStr | None = None
    AutoAccept: StrictBool | None = None
    AfterContactWorkTimeLimit: StrictInt | None = None
    DeskPhoneNumber: StrictStr | None = None
    PersistentConnection: StrictBool | None = None
