from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MemoryDBAuthentication(BaseModel):
    Type: StrictStr | None = None
    PasswordCount: StrictInt | None = None
