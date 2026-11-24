from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueRunStatementRequest(BaseModel):
    SessionId: StrictStr
    Code: StrictStr
    RequestOrigin: StrictStr | None = None
