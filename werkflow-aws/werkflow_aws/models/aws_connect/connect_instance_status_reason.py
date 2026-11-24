from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectInstanceStatusReason(BaseModel):
    Message: StrictStr | None = None
