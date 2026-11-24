from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStopColumnStatisticsTaskRunScheduleRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    CatalogID: StrictStr | None = None
