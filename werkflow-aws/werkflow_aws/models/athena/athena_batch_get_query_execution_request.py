from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaBatchGetQueryExecutionRequest(BaseModel):
    QueryExecutionIds: list[StrictStr]
