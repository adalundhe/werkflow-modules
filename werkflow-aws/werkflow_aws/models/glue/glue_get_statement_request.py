from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueGetStatementRequest(BaseModel):
    SessionId: StrictStr
    Id: StrictInt
    RequestOrigin: StrictStr | None = None
