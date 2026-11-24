from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueCancelStatementRequest(BaseModel):
    SessionId: StrictStr
    Id: StrictInt
    RequestOrigin: StrictStr | None = None
