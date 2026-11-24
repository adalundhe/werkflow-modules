from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimestreamQueryCancelQueryRequest(BaseModel):
    QueryId: StrictStr
