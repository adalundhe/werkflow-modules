from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectReleasePhoneNumberRequest(BaseModel):
    PhoneNumberId: StrictStr
    ClientToken: StrictStr | None = None
