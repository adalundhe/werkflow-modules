from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaUpdatePreparedStatementRequest(BaseModel):
    StatementName: StrictStr
    WorkGroup: StrictStr
    QueryStatement: StrictStr
    Description: StrictStr | None = None
