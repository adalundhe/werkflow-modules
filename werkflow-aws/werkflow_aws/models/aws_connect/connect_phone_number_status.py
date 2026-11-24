from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectPhoneNumberStatus(BaseModel):
    Status: StrictStr | None = None
    Message: StrictStr | None = None
