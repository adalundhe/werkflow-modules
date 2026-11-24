from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPhoneNumberConfig(BaseModel):
    Channel: StrictStr | None = None
    PhoneType: StrictStr | None = None
    PhoneNumber: StrictStr | None = None
