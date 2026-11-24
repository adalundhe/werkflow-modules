from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectionCredentials(BaseModel):
    ConnectionToken: StrictStr | None = None
    Expiry: StrictStr | None = None
