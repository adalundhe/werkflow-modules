from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPhoneNumberQuickConnectConfig(BaseModel):
    PhoneNumber: StrictStr | None = None
