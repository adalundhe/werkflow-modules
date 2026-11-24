from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaBatchGetPreparedStatementRequest(BaseModel):
    PreparedStatementNames: list[StrictStr]
    WorkGroup: StrictStr
