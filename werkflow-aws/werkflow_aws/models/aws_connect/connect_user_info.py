from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectUserInfo(BaseModel):
    UserId: StrictStr | None = None
