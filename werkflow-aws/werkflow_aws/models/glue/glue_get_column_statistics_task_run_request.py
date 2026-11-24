from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetColumnStatisticsTaskRunRequest(BaseModel):
    ColumnStatisticsTaskRunId: StrictStr
