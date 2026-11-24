from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectWebsocket(BaseModel):
    Url: StrictStr | None = None
    ConnectionExpiry: StrictStr | None = None
