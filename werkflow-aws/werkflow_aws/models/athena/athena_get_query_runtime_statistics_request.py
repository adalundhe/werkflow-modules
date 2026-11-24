from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AthenaGetQueryRuntimeStatisticsRequest(BaseModel):
    QueryExecutionId: StrictStr
