from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEmailRecipient(BaseModel):
    Address: StrictStr | None = None
    DisplayName: StrictStr | None = None
