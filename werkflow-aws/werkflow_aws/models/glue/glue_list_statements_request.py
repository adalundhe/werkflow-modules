from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueListStatementsRequest(BaseModel):
    SessionId: StrictStr
    RequestOrigin: StrictStr | None = None
    NextToken: StrictStr | None = None
