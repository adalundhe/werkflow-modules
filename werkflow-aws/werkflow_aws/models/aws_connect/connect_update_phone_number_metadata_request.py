from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUpdatePhoneNumberMetadataRequest(BaseModel):
    PhoneNumberId: StrictStr
    PhoneNumberDescription: StrictStr | None = None
    ClientToken: StrictStr | None = None
