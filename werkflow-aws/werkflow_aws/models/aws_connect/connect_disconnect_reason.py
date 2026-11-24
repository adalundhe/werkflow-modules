from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDisconnectReason(BaseModel):
    Code: StrictStr | None = None
