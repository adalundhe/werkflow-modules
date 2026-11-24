from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEmailAddressInfo(BaseModel):
    EmailAddress: StrictStr
    DisplayName: StrictStr | None = None
