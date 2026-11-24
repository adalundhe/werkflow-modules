from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TransferUserDetails(BaseModel):
    UserName: StrictStr | None = None
    ServerId: StrictStr | None = None
    SessionId: StrictStr | None = None
