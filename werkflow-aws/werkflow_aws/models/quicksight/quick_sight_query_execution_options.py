from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightQueryExecutionOptions(BaseModel):
    QueryExecutionMode: StrictStr | None = None
